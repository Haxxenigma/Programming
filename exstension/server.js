const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;
const apiKey = 'xxx';

app.use(express.json());

app.post('/check', async (req, res) => {
    const clientUrl = encodeURIComponent(req.body.currentURL);
    const url = `https://api.metadefender.com/v4/url/${clientUrl}`;

    try {
        const result = await axios.get(url, {
            headers: {
                apikey: apiKey,
            },
        });

        const phishingResult = result.data.lookup_results.detected_by;
        let verdict;
        let danger;

        if (phishingResult > 0) {
            verdict = 'Данный сайт может являться фишинговым. Не передавайте свои данные!';
            danger = true;
        } else {
            verdict = 'Данный сайт скорее всего не является фишинговым';
            danger = false;
        }

        res.json({ verdict, danger });
    } catch (err) {
        console.error('Error: ', err.message);
        res.status(500).json({ error: err.message });
    }
});

app.listen(port);