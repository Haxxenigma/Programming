from bs4 import BeautifulSoup
from openai import OpenAI
from requests import get
from config import api_key

gpt = OpenAI(api_key=api_key)


async def rewrite_news(prompt):
    completion = gpt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Твоя задача - перефразировать и сократить данные тебе новости по кибербезопасности так, \
             чтобы данные новости были понятны даже для простых граждан, которые ничего не понимают в кибербезопасности",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message.content


async def parse_news(base_url, path, links_selector, content_selector):
    res = get(base_url + path)
    soup = BeautifulSoup(res.content, "html.parser")

    links = soup.select(links_selector)

    for index, link in enumerate(links):
        if index == 3:
            break

        fullPath = base_url + link["href"]
        res = get(fullPath)
        article = BeautifulSoup(res.content, "html.parser")

        article_paragraphs = article.select(content_selector)
        article_content = []

        for article_paragraph in article_paragraphs:
            article_content.append(article_paragraph.text)

        rewrited_news = await rewrite_news(" ".join(article_content))

        yield {
            "title": link.text,
            "content": rewrited_news,
            "link": fullPath,
        }
