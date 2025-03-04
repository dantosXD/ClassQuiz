from unittest import IsolatedAsyncioTestCase
from classquiz.kahoot_importer.search import search


class Test(IsolatedAsyncioTestCase):
    async def test_search(self):
        res = await search(query="Python", limit=100)
        self.assertEqual(len(res.entities), 100)
        await search(query="Test Quiz", limit=100)
        await search(query="Biologie", limit=100)
        await search(query="Chemie", limit=100)
        await search(query="Deutsch", limit=100)
        await search(query="Mathe", limit=100)
        await search(query="Englisch", limit=100)
        await search(query="Barbie", limit=100)
        await search(query="Internet", limit=100)
        await search(query="Windows", limit=100)
        res2 = await search(query="Python", limit=100)
        res2_ids = [str(e.card.uuid) for e in res2.entities]
        print(res2_ids)
