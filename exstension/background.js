const button = document.querySelector('.button');
const resultOk = document.querySelector('.result-ok');
const resultDanger = document.querySelector('.result-danger');

button.addEventListener('click', async () => {
    button.innerHTML = 'Проверка...';
    const [tab] = await chrome.tabs.query({
        active: true,
        lastFocusedWindow: true,
    });

    const url = 'https://0efb57d3-e2d1-49fe-a247-1c082c354975-00-398g0g2f9ft6p.sisko.replit.dev/check';

    try {
        const res = await fetch(url, {
            method: 'POST',
            body: JSON.stringify({
                currentURL: tab.url,
            }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        const data = await res.json();
        button.innerHTML = 'Проверить';
        if (data.danger) {
            resultDanger.innerHTML = data.verdict;
        } else {
            resultOk.innerHTML = data.verdict;
        }
    } catch (err) {
        console.error(err);
        resultDanger.innerHTML = 'Произошла ошибка, перезагрузите страницу и повторите попытку';
    }
});