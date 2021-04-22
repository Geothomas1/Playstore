import scrapy
from ..items import PlaystoreDatasetItem
main_list=[]
class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps/collection/cluster?clp=SjYKKgokcHJvbW90aW9uXzMwMDA3OTFfbmV3X3JlbGVhc2VzX2dhbWVzEEoYAxIER0FNRToCCAI%3D:S:ANO1ljJYK2k&gsr=CjhKNgoqCiRwcm9tb3Rpb25fMzAwMDc5MV9uZXdfcmVsZWFzZXNfZ2FtZXMQShgDEgRHQU1FOgIIAg%3D%3D:S:ANO1ljICr10',
        'https://play.google.com/store/apps/collection/cluster?clp=SjMKJwohcHJvbW90aW9uXzMwMDE3ZWVfdW5kZXIyNW1iX2dhbWVzEEoYAxIER0FNRToCCAI%3D:S:ANO1ljJryxM&gsr=CjVKMwonCiFwcm9tb3Rpb25fMzAwMTdlZV91bmRlcjI1bWJfZ2FtZXMQShgDEgRHQU1FOgIIAg%3D%3D:S:ANO1ljIwjzE',
        'https://play.google.com/store/apps/collection/cluster?clp=SjMKJwohcHJvbW90aW9uX2dhbWVzX3dlX2FyZV9wbGF5aW5nX2luEEoYAxIER0FNRToCCAI%3D:S:ANO1ljJHJao&gsr=CjVKMwonCiFwcm9tb3Rpb25fZ2FtZXNfd2VfYXJlX3BsYXlpbmdfaW4QShgDEgRHQU1FOgIIAg%3D%3D:S:ANO1ljIfNTU',
        'https://play.google.com/store/apps/collection/cluster?clp=SikKHQoXcHJvbW90aW9uX3JhbWFkYW5fZ2FtZXMQShgDEgRHQU1FOgIIAg%3D%3D:S:ANO1ljI8k8s&gsr=CitKKQodChdwcm9tb3Rpb25fcmFtYWRhbl9nYW1lcxBKGAMSBEdBTUU6AggC:S:ANO1ljJUdn8',
        'https://play.google.com/store/apps/collection/cluster?clp=SkcKOwo1cHJvbW90aW9uXzMwMDJhYWZfZ2FtZXNfaW5kaWVfY29ybmVyX3N0b3JlX2NvbGxlY3Rpb24QShgDEgRHQU1FOgIIAg%3D%3D:S:ANO1ljLm9rw&gsr=CklKRwo7CjVwcm9tb3Rpb25fMzAwMmFhZl9nYW1lc19pbmRpZV9jb3JuZXJfc3RvcmVfY29sbGVjdGlvbhBKGAMSBEdBTUU6AggC:S:ANO1ljLN9Sc',
        'https://play.google.com/store/apps/collection/cluster?clp=Sj0KMQorcHJvbW90aW9uXzMwMDAwMDBkNTFfcHJlX3JlZ2lzdHJhdGlvbl9nYW1lcxBKGAMSBEdBTUU6AggC:S:ANO1ljLVQMI&gsr=Cj9KPQoxCitwcm9tb3Rpb25fMzAwMDAwMGQ1MV9wcmVfcmVnaXN0cmF0aW9uX2dhbWVzEEoYAxIER0FNRToCCAI%3D:S:ANO1ljJICV4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX0FDVElPThAHGAM%3D:S:ANO1ljKHNjI&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfQUNUSU9OEAcYAw%3D%3D:S:ANO1ljLUxfQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX0FDVElPThAHGAM%3D:S:ANO1ljLH0kM&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfQUNUSU9OEAcYAw%3D%3D:S:ANO1ljIdBNk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfQUNUSU9OEAcYAw%3D%3D:S:ANO1ljIOh7o&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9BQ1RJT04QBxgD:S:ANO1ljLWGVQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9HQU1FX0FEVkVOVFVSRRAHGAM%3D:S:ANO1ljJV7FQ&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0dBTUVfQURWRU5UVVJFEAcYAw%3D%3D:S:ANO1ljIcQUo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfcGFpZF9HQU1FX0FEVkVOVFVSRRAHGAM%3D:S:ANO1ljKjB_A&gsr=CinSDiYKJAoedG9wc2VsbGluZ19wYWlkX0dBTUVfQURWRU5UVVJFEAcYAw%3D%3D:S:ANO1ljJuB_8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcGdyb3NzaW5nX0dBTUVfQURWRU5UVVJFEAcYAw%3D%3D:S:ANO1ljIiDUs&gsr=CiXSDiIKIAoadG9wZ3Jvc3NpbmdfR0FNRV9BRFZFTlRVUkUQBxgD:S:ANO1ljIgZ0k',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX0FSQ0FERRAHGAM%3D:S:ANO1ljIshgI&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfQVJDQURFEAcYAw%3D%3D:S:ANO1ljJq_Gc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX0FSQ0FERRAHGAM%3D:S:ANO1ljIhZHI&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfQVJDQURFEAcYAw%3D%3D:S:ANO1ljKAU-U',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfQVJDQURFEAcYAw%3D%3D:S:ANO1ljIu1QY&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9BUkNBREUQBxgD:S:ANO1ljKv_1M',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcHNlbGxpbmdfZnJlZV9HQU1FX0JPQVJEEAcYAw%3D%3D:S:ANO1ljL4-C4&gsr=CiXSDiIKIAoadG9wc2VsbGluZ19mcmVlX0dBTUVfQk9BUkQQBxgD:S:ANO1ljKCMxA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcHNlbGxpbmdfcGFpZF9HQU1FX0JPQVJEEAcYAw%3D%3D:S:ANO1ljJzXAU&gsr=CiXSDiIKIAoadG9wc2VsbGluZ19wYWlkX0dBTUVfQk9BUkQQBxgD:S:ANO1ljKlrPM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcGdyb3NzaW5nX0dBTUVfQk9BUkQQBxgD:S:ANO1ljKb0xc&gsr=CiHSDh4KHAoWdG9wZ3Jvc3NpbmdfR0FNRV9CT0FSRBAHGAM%3D:S:ANO1ljKiHwY',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfZnJlZV9HQU1FX0NBUkQQBxgD:S:ANO1ljLIZ98&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19mcmVlX0dBTUVfQ0FSRBAHGAM%3D:S:ANO1ljJ_lBQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfcGFpZF9HQU1FX0NBUkQQBxgD:S:ANO1ljJscys&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19wYWlkX0dBTUVfQ0FSRBAHGAM%3D:S:ANO1ljJdjQU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFXRvcGdyb3NzaW5nX0dBTUVfQ0FSRBAHGAM%3D:S:ANO1ljJ4nPw&gsr=CiDSDh0KGwoVdG9wZ3Jvc3NpbmdfR0FNRV9DQVJEEAcYAw%3D%3D:S:ANO1ljKHMJA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX0NBU0lOTxAHGAM%3D:S:ANO1ljLgBLI&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfQ0FTSU5PEAcYAw%3D%3D:S:ANO1ljKRt4Q',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX0NBU0lOTxAHGAM%3D:S:ANO1ljKKXS8&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfQ0FTSU5PEAcYAw%3D%3D:S:ANO1ljKKlDQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfQ0FTSU5PEAcYAw%3D%3D:S:ANO1ljIYPss&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9DQVNJTk8QBxgD:S:ANO1ljJRAWc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX0NBU1VBTBAHGAM%3D:S:ANO1ljLV380&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfQ0FTVUFMEAcYAw%3D%3D:S:ANO1ljIYYsk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX0NBU1VBTBAHGAM%3D:S:ANO1ljKu4yM&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfQ0FTVUFMEAcYAw%3D%3D:S:ANO1ljK2Y3o',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfQ0FTVUFMEAcYAw%3D%3D:S:ANO1ljLig8k&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9DQVNVQUwQBxgD:S:ANO1ljLsHHI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4oCiYKIHRvcHNlbGxpbmdfZnJlZV9HQU1FX0VEVUNBVElPTkFMEAcYAw%3D%3D:S:ANO1ljIXePQ&gsr=CivSDigKJgogdG9wc2VsbGluZ19mcmVlX0dBTUVfRURVQ0FUSU9OQUwQBxgD:S:ANO1ljJyrL8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4oCiYKIHRvcHNlbGxpbmdfcGFpZF9HQU1FX0VEVUNBVElPTkFMEAcYAw%3D%3D:S:ANO1ljKfMYQ&gsr=CivSDigKJgogdG9wc2VsbGluZ19wYWlkX0dBTUVfRURVQ0FUSU9OQUwQBxgD:S:ANO1ljKesRA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHHRvcGdyb3NzaW5nX0dBTUVfRURVQ0FUSU9OQUwQBxgD:S:ANO1ljKggmQ&gsr=CifSDiQKIgocdG9wZ3Jvc3NpbmdfR0FNRV9FRFVDQVRJT05BTBAHGAM%3D:S:ANO1ljJAuB8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcHNlbGxpbmdfZnJlZV9HQU1FX01VU0lDEAcYAw%3D%3D:S:ANO1ljLRvvI&gsr=CiXSDiIKIAoadG9wc2VsbGluZ19mcmVlX0dBTUVfTVVTSUMQBxgD:S:ANO1ljJI1UU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcHNlbGxpbmdfcGFpZF9HQU1FX01VU0lDEAcYAw%3D%3D:S:ANO1ljLaZUI&gsr=CiXSDiIKIAoadG9wc2VsbGluZ19wYWlkX0dBTUVfTVVTSUMQBxgD:S:ANO1ljK7800',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcGdyb3NzaW5nX0dBTUVfTVVTSUMQBxgD:S:ANO1ljKCSZQ&gsr=CiHSDh4KHAoWdG9wZ3Jvc3NpbmdfR0FNRV9NVVNJQxAHGAM%3D:S:ANO1ljLWeOY',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX1BVWlpMRRAHGAM%3D:S:ANO1ljLYuNA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfUFVaWkxFEAcYAw%3D%3D:S:ANO1ljIyFv8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX1BVWlpMRRAHGAM%3D:S:ANO1ljIFZPM&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfUFVaWkxFEAcYAw%3D%3D:S:ANO1ljIYoBk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfUFVaWkxFEAcYAw%3D%3D:S:ANO1ljKfwXc&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9QVVpaTEUQBxgD:S:ANO1ljIxTd0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX1JBQ0lORxAHGAM%3D:S:ANO1ljKlRGU&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfUkFDSU5HEAcYAw%3D%3D:S:ANO1ljIWYJI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX1JBQ0lORxAHGAM%3D:S:ANO1ljLklZk&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfUkFDSU5HEAcYAw%3D%3D:S:ANO1ljJvXBg',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfUkFDSU5HEAcYAw%3D%3D:S:ANO1ljKIqj8&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9SQUNJTkcQBxgD:S:ANO1ljIjOww',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfZnJlZV9HQU1FX1JPTEVfUExBWUlORxAHGAM%3D:S:ANO1ljJawN8&gsr=CizSDikKJwohdG9wc2VsbGluZ19mcmVlX0dBTUVfUk9MRV9QTEFZSU5HEAcYAw%3D%3D:S:ANO1ljISF1w',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfcGFpZF9HQU1FX1JPTEVfUExBWUlORxAHGAM%3D:S:ANO1ljLiiew&gsr=CizSDikKJwohdG9wc2VsbGluZ19wYWlkX0dBTUVfUk9MRV9QTEFZSU5HEAcYAw%3D%3D:S:ANO1ljJ0Gwk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcGdyb3NzaW5nX0dBTUVfUk9MRV9QTEFZSU5HEAcYAw%3D%3D:S:ANO1ljICzGM&gsr=CijSDiUKIwoddG9wZ3Jvc3NpbmdfR0FNRV9ST0xFX1BMQVlJTkcQBxgD:S:ANO1ljLpYvY',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfZnJlZV9HQU1FX1NJTVVMQVRJT04QBxgD:S:ANO1ljKreHA&gsr=CirSDicKJQofdG9wc2VsbGluZ19mcmVlX0dBTUVfU0lNVUxBVElPThAHGAM%3D:S:ANO1ljI7FRI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfcGFpZF9HQU1FX1NJTVVMQVRJT04QBxgD:S:ANO1ljIt5SI&gsr=CirSDicKJQofdG9wc2VsbGluZ19wYWlkX0dBTUVfU0lNVUxBVElPThAHGAM%3D:S:ANO1ljKeTxs',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcGdyb3NzaW5nX0dBTUVfU0lNVUxBVElPThAHGAM%3D:S:ANO1ljK3ulU&gsr=CibSDiMKIQobdG9wZ3Jvc3NpbmdfR0FNRV9TSU1VTEFUSU9OEAcYAw%3D%3D:S:ANO1ljKCLo8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX1NQT1JUUxAHGAM%3D:S:ANO1ljK19eE&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfU1BPUlRTEAcYAw%3D%3D:S:ANO1ljJKUZM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX1NQT1JUUxAHGAM%3D:S:ANO1ljIGfKM&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfU1BPUlRTEAcYAw%3D%3D:S:ANO1ljLc9sU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfU1BPUlRTEAcYAw%3D%3D:S:ANO1ljL9jds&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9TUE9SVFMQBxgD:S:ANO1ljIN048',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfZnJlZV9HQU1FX1NUUkFURUdZEAcYAw%3D%3D:S:ANO1ljIuwtQ&gsr=CijSDiUKIwoddG9wc2VsbGluZ19mcmVlX0dBTUVfU1RSQVRFR1kQBxgD:S:ANO1ljLpyj4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfcGFpZF9HQU1FX1NUUkFURUdZEAcYAw%3D%3D:S:ANO1ljI3COs&gsr=CijSDiUKIwoddG9wc2VsbGluZ19wYWlkX0dBTUVfU1RSQVRFR1kQBxgD:S:ANO1ljIhVjE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcGdyb3NzaW5nX0dBTUVfU1RSQVRFR1kQBxgD:S:ANO1ljIZnLc&gsr=CiTSDiEKHwoZdG9wZ3Jvc3NpbmdfR0FNRV9TVFJBVEVHWRAHGAM%3D:S:ANO1ljIBios',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9HQU1FX1RSSVZJQRAHGAM%3D:S:ANO1ljLw164&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0dBTUVfVFJJVklBEAcYAw%3D%3D:S:ANO1ljIUmRc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9HQU1FX1RSSVZJQRAHGAM%3D:S:ANO1ljJeZh8&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX0dBTUVfVFJJVklBEAcYAw%3D%3D:S:ANO1ljKHdVE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0dBTUVfVFJJVklBEAcYAw%3D%3D:S:ANO1ljIwnF8&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfR0FNRV9UUklWSUEQBxgD:S:ANO1ljIPUNQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfZnJlZV9HQU1FX1dPUkQQBxgD:S:ANO1ljLuO2k&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19mcmVlX0dBTUVfV09SRBAHGAM%3D:S:ANO1ljIqSWE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfcGFpZF9HQU1FX1dPUkQQBxgD:S:ANO1ljJM7Hg&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19wYWlkX0dBTUVfV09SRBAHGAM%3D:S:ANO1ljJLmvc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFXRvcGdyb3NzaW5nX0dBTUVfV09SRBAHGAM%3D:S:ANO1ljKW788&gsr=CiDSDh0KGwoVdG9wZ3Jvc3NpbmdfR0FNRV9XT1JEEAcYAw%3D%3D:S:ANO1ljKhGzM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9GQU1JTFkQBxgD:S:ANO1ljLJuUM&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0ZBTUlMWRAHGAM%3D:S:ANO1ljID-6I',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9GQU1JTFkQBxgD:S:ANO1ljK6OuI&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0ZBTUlMWRAHGAM%3D:S:ANO1ljKusJQ',
        'https://play.google.com/store/apps/collection/cluster?clp=SkUKNwoxcHJvbW90aW9uX2FnZXJhbmdlMl8zMDAxNzM4X3BvcHVsYXJhcHBzZ2FtZXNfNnRvOBBKGAMSBkZBTUlMWToCCAM%3D:S:ANO1ljIb_qQ&gsr=CkdKRQo3CjFwcm9tb3Rpb25fYWdlcmFuZ2UyXzMwMDE3MzhfcG9wdWxhcmFwcHNnYW1lc182dG84EEoYAxIGRkFNSUxZOgIIAw%3D%3D:S:ANO1ljK4-R8',
        'https://play.google.com/store/apps/collection/cluster?clp=SkEKMwotcHJvbW90aW9uX2FnZXJhbmdlMl8zMDAxNzNiX3lvdW5ncmVhZGVyc182dG84EEoYAxIGRkFNSUxZOgIIAw%3D%3D:S:ANO1ljIWNvk&gsr=CkNKQQozCi1wcm9tb3Rpb25fYWdlcmFuZ2UyXzMwMDE3M2JfeW91bmdyZWFkZXJzXzZ0bzgQShgDEgZGQU1JTFk6AggD:S:ANO1ljJh3nM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9GQU1JTFkQBxgD:S:ANO1ljLJuUM&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0ZBTUlMWRAHGAM%3D:S:ANO1ljID-6I',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9GQU1JTFkQBxgD:S:ANO1ljK6OuI&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0ZBTUlMWRAHGAM%3D:S:ANO1ljKusJQ',
        'https://play.google.com/store/apps/collection/cluster?clp=SjwKLgoocHJvbW90aW9uX2ZhbWlseXNhZmVfMzAwMThiM19uZXdfdXBkYXRlZBBKGAMSBkZBTUlMWToCCAM%3D:S:ANO1ljL5G8U&gsr=Cj5KPAouCihwcm9tb3Rpb25fZmFtaWx5c2FmZV8zMDAxOGIzX25ld191cGRhdGVkEEoYAxIGRkFNSUxZOgIIAw%3D%3D:S:ANO1ljJg2TY',
        'https://play.google.com/store/apps/collection/cluster?clp=SjoKLAomcHJvbW90aW9uX2ZhbWlseV9raWRzYXRob21lX2ZhbWlseWhvbWUQShgDEgZGQU1JTFk6AggD:S:ANO1ljI1F1s&gsr=CjxKOgosCiZwcm9tb3Rpb25fZmFtaWx5X2tpZHNhdGhvbWVfZmFtaWx5aG9tZRBKGAMSBkZBTUlMWToCCAM%3D:S:ANO1ljJMyP4',
        'https://play.google.com/store/apps/collection/cluster?clp=SlAKQgo8cHJvbW90aW9uX2ZhbWlseXNhZmVfZHVtYmxlc3RvcmVfYXV0aXNtX2F3YXJlbmVzc19jb2xsZWN0aW9uEEoYAxIGRkFNSUxZOgIIAw%3D%3D:S:ANO1ljJ9UpM&gsr=ClJKUApCCjxwcm9tb3Rpb25fZmFtaWx5c2FmZV9kdW1ibGVzdG9yZV9hdXRpc21fYXdhcmVuZXNzX2NvbGxlY3Rpb24QShgDEgZGQU1JTFk6AggD:S:ANO1ljIEF5U',
        ]

    def parse(self, response):
        apps=PlaystoreDatasetItem()
        dev_link=[]
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        app_link=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract()  
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        #apps['app_name']=app_name
        # apps['app_developer']=app_developer
        # apps['app_link']=app_link
        #apps['app_developer_link']=app_developer_link
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
        #print(dev_link)
        for x in dev_link:
            main_list.append(x)
        yield {'link':main_list}
        print(len(main_list))
    




   