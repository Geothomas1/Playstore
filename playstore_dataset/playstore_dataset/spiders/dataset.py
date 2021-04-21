import scrapy
from ..items import PlaystoreDatasetItem
main_list=[]
class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9BUlRfQU5EX0RFU0lHThAHGAM%3D:S:ANO1ljKKwsU&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljK_3F0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcGdyb3NzaW5nX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljIXYIY&gsr=CiXSDiIKIAoadG9wZ3Jvc3NpbmdfQVJUX0FORF9ERVNJR04QBxgD:S:ANO1ljIQjsw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHW1vdmVyc19zaGFrZXJzX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljLIuvY&gsr=CijSDiUKIwodbW92ZXJzX3NoYWtlcnNfQVJUX0FORF9ERVNJR04QBxgD:S:ANO1ljI5X-E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfcGFpZF9BUlRfQU5EX0RFU0lHThAHGAM%3D:S:ANO1ljLn4cw&gsr=CinSDiYKJAoedG9wc2VsbGluZ19wYWlkX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljK90S4',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsoCiYKIHByb21vdGlvbl9hcl9zdG9yZWNhdGVnb3J5X2FyZWR1EEoYAw%3D%3D:S:ANO1ljLVBCs&gsr=CivqCygKJgogcHJvbW90aW9uX2FyX3N0b3JlY2F0ZWdvcnlfYXJlZHUQShgD:S:ANO1ljIwMKs',
        'https://play.google.com/store/apps/collection/cluster?clp=6gstCisKJXByb21vdGlvbl9kYXlkcmVhbV9hcl9jb3ZpZF9lZHVjYXRpb24QShgD:S:ANO1ljIr61g&gsr=CjDqCy0KKwolcHJvbW90aW9uX2RheWRyZWFtX2FyX2NvdmlkX2VkdWNhdGlvbhBKGAM%3D:S:ANO1ljJnKTg',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsxCi8KKXByb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2Jlc3RvZmFyEEoYAw%3D%3D:S:ANO1ljI3sew&gsr=CjTqCzEKLwopcHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYmVzdG9mYXIQShgD:S:ANO1ljJFdTc',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsvCi0KJ3Byb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2FyYXBwcxBKGAM%3D:S:ANO1ljLDFOc&gsr=CjLqCy8KLQoncHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYXJhcHBzEEoYAw%3D%3D:S:ANO1ljKjMrE',
        'https://play.google.com/store/apps/collection/cluster?clp=6gswCi4KKHByb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2FyZ2FtZXMQShgD:S:ANO1ljID8iM&gsr=CjPqCzAKLgoocHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYXJnYW1lcxBKGAM%3D:S:ANO1ljKbARQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfZnJlZV9BVVRPX0FORF9WRUhJQ0xFUxAHGAM%3D:S:ANO1ljL6W3A&gsr=CizSDikKJwohdG9wc2VsbGluZ19mcmVlX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljI4VxE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcGdyb3NzaW5nX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljKFzY4&gsr=CijSDiUKIwoddG9wZ3Jvc3NpbmdfQVVUT19BTkRfVkVISUNMRVMQBxgD:S:ANO1ljLTBqo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4oCiYKIG1vdmVyc19zaGFrZXJzX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljJrBjA&gsr=CivSDigKJgogbW92ZXJzX3NoYWtlcnNfQVVUT19BTkRfVkVISUNMRVMQBxgD:S:ANO1ljK4yRw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfcGFpZF9BVVRPX0FORF9WRUhJQ0xFUxAHGAM%3D:S:ANO1ljI75E8&gsr=CizSDikKJwohdG9wc2VsbGluZ19wYWlkX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljJyZ6w',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9CRUFVVFkQBxgD:S:ANO1ljLNjvk&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0JFQVVUWRAHGAM%3D:S:ANO1ljIGC5s',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0JFQVVUWRAHGAM%3D:S:ANO1ljLcvug&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfQkVBVVRZEAcYAw%3D%3D:S:ANO1ljKI1x8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0JFQVVUWRAHGAM%3D:S:ANO1ljI3S4E&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfQkVBVVRZEAcYAw%3D%3D:S:ANO1ljKfIuU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9CRUFVVFkQBxgD:S:ANO1ljIF2qM&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0JFQVVUWRAHGAM%3D:S:ANO1ljIZfJ0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfZnJlZV9CT09LU19BTkRfUkVGRVJFTkNFEAcYAw%3D%3D:S:ANO1ljJ2D4g&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19mcmVlX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljIiZrU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcGdyb3NzaW5nX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljL_ufs&gsr=CirSDicKJQofdG9wZ3Jvc3NpbmdfQk9PS1NfQU5EX1JFRkVSRU5DRRAHGAM%3D:S:ANO1ljJw454',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKIm1vdmVyc19zaGFrZXJzX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljL_ZcY&gsr=Ci3SDioKKAoibW92ZXJzX3NoYWtlcnNfQk9PS1NfQU5EX1JFRkVSRU5DRRAHGAM%3D:S:ANO1ljI0OG0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfcGFpZF9CT09LU19BTkRfUkVGRVJFTkNFEAcYAw%3D%3D:S:ANO1ljLRUDc&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19wYWlkX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljIa7_Y',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfZnJlZV9CVVNJTkVTUxAHGAM%3D:S:ANO1ljLX_9I&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19mcmVlX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljIQk5E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcGdyb3NzaW5nX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljKjFx8&gsr=Ch_SDhwKGgoUdG9wZ3Jvc3NpbmdfQlVTSU5FU1MQBxgD:S:ANO1ljI1NO8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF21vdmVyc19zaGFrZXJzX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljKNUP4&gsr=CiLSDh8KHQoXbW92ZXJzX3NoYWtlcnNfQlVTSU5FU1MQBxgD:S:ANO1ljICTN4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfcGFpZF9CVVNJTkVTUxAHGAM%3D:S:ANO1ljILu9E&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19wYWlkX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljL4cI8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9DT01JQ1MQBxgD:S:ANO1ljITZ68&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0NPTUlDUxAHGAM%3D:S:ANO1ljKZ2sc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0NPTUlDUxAHGAM%3D:S:ANO1ljLTs7k&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfQ09NSUNTEAcYAw%3D%3D:S:ANO1ljIooKo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0NPTUlDUxAHGAM%3D:S:ANO1ljLvqPo&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfQ09NSUNTEAcYAw%3D%3D:S:ANO1ljLcI_E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9DT01JQ1MQBxgD:S:ANO1ljJmiCw&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0NPTUlDUxAHGAM%3D:S:ANO1ljILjYE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfZnJlZV9DT01NVU5JQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljJhLKU&gsr=CijSDiUKIwoddG9wc2VsbGluZ19mcmVlX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljIDVBk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcGdyb3NzaW5nX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljJi3A0&gsr=CiTSDiEKHwoZdG9wZ3Jvc3NpbmdfQ09NTVVOSUNBVElPThAHGAM%3D:S:ANO1ljJ7Efo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHG1vdmVyc19zaGFrZXJzX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljKs21c&gsr=CifSDiQKIgocbW92ZXJzX3NoYWtlcnNfQ09NTVVOSUNBVElPThAHGAM%3D:S:ANO1ljJUGKU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfcGFpZF9DT01NVU5JQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljLE4oc&gsr=CijSDiUKIwoddG9wc2VsbGluZ19wYWlkX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljI8da0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9EQVRJTkcQBxgD:S:ANO1ljJ0qxs&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0RBVElORxAHGAM%3D:S:ANO1ljJvMRw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0RBVElORxAHGAM%3D:S:ANO1ljJoXc4&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfREFUSU5HEAcYAw%3D%3D:S:ANO1ljLZt7Q',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0RBVElORxAHGAM%3D:S:ANO1ljJZo_A&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfREFUSU5HEAcYAw%3D%3D:S:ANO1ljLwxJ8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9EQVRJTkcQBxgD:S:ANO1ljI3voA&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0RBVElORxAHGAM%3D:S:ANO1ljJPlCU',
        'https://play.google.com/store/apps/collection/cluster?clp=an8KNgowcHJvbW90aW9uXzMwMDI1ZTFfZGF5ZHJlYW1fc3RvcmVjYXRlZ29yeV90b3BhcHBzEAcYAxJFCj92cl90b3BfZGV2aWNlX2ZlYXR1cmVkX2NhdGVnb3J5X2FwcHNfX18xX3Byb21vXzE1NDMzNTYyOTQ1NzYwMDAQDBgD:S:ANO1ljIyjUI&gsr=CoEBan8KNgowcHJvbW90aW9uXzMwMDI1ZTFfZGF5ZHJlYW1fc3RvcmVjYXRlZ29yeV90b3BhcHBzEAcYAxJFCj92cl90b3BfZGV2aWNlX2ZlYXR1cmVkX2NhdGVnb3J5X2FwcHNfX18xX3Byb21vXzE1NDMzNTYyOTQ1NzYwMDAQDBgD:S:ANO1ljL4zsA',
        'https://play.google.com/store/apps/collection/cluster?clp=aoABCjcKMXByb21vdGlvbl8zMDAyNWUxX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfdG9wZ2FtZXMQBxgDEkUKP3ZyX3RvcF9kZXZpY2VfZmVhdHVyZWRfY2F0ZWdvcnlfYXBwc19fXzJfcHJvbW9fMTU0MzM1NjI5NDU3NjAwMBAMGAM%3D:S:ANO1ljKEE0U&gsr=CoMBaoABCjcKMXByb21vdGlvbl8zMDAyNWUxX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfdG9wZ2FtZXMQBxgDEkUKP3ZyX3RvcF9kZXZpY2VfZmVhdHVyZWRfY2F0ZWdvcnlfYXBwc19fXzJfcHJvbW9fMTU0MzM1NjI5NDU3NjAwMBAMGAM%3D:S:ANO1ljI5J0o',
        'https://play.google.com/store/apps/collection/cluster?clp=aogBCj8KOXByb21vdGlvbl8yMDAyNWUxX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfdG9wZW50ZXJ0YWlubWVudBAHGAMSRQo_dnJfdG9wX2RldmljZV9mZWF0dXJlZF9jYXRlZ29yeV9hcHBzX19fM19wcm9tb18xNTQzMzU2Mjk0NTc2MDAwEAwYAw%3D%3D:S:ANO1ljKMgOs&gsr=CosBaogBCj8KOXByb21vdGlvbl8yMDAyNWUxX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfdG9wZW50ZXJ0YWlubWVudBAHGAMSRQo_dnJfdG9wX2RldmljZV9mZWF0dXJlZF9jYXRlZ29yeV9hcHBzX19fM19wcm9tb18xNTQzMzU2Mjk0NTc2MDAwEAwYAw%3D%3D:S:ANO1ljJoSYc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfZnJlZV9FRFVDQVRJT04QBxgD:S:ANO1ljKK35I&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19mcmVlX0VEVUNBVElPThAHGAM%3D:S:ANO1ljIr054',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFXRvcGdyb3NzaW5nX0VEVUNBVElPThAHGAM%3D:S:ANO1ljLV7Mw&gsr=CiDSDh0KGwoVdG9wZ3Jvc3NpbmdfRURVQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljJ72yQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGG1vdmVyc19zaGFrZXJzX0VEVUNBVElPThAHGAM%3D:S:ANO1ljIrwsE&gsr=CiPSDiAKHgoYbW92ZXJzX3NoYWtlcnNfRURVQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljJTs4I',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfcGFpZF9FRFVDQVRJT04QBxgD:S:ANO1ljIrdxA&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19wYWlkX0VEVUNBVElPThAHGAM%3D:S:ANO1ljL0W4s',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfZnJlZV9FTlRFUlRBSU5NRU5UEAcYAw%3D%3D:S:ANO1ljL34tM&gsr=CijSDiUKIwoddG9wc2VsbGluZ19mcmVlX0VOVEVSVEFJTk1FTlQQBxgD:S:ANO1ljKOzjg',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcGdyb3NzaW5nX0VOVEVSVEFJTk1FTlQQBxgD:S:ANO1ljLyoR8&gsr=CiTSDiEKHwoZdG9wZ3Jvc3NpbmdfRU5URVJUQUlOTUVOVBAHGAM%3D:S:ANO1ljKhA3M',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHG1vdmVyc19zaGFrZXJzX0VOVEVSVEFJTk1FTlQQBxgD:S:ANO1ljJADgw&gsr=CifSDiQKIgocbW92ZXJzX3NoYWtlcnNfRU5URVJUQUlOTUVOVBAHGAM%3D:S:ANO1ljL92p4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfcGFpZF9FTlRFUlRBSU5NRU5UEAcYAw%3D%3D:S:ANO1ljIrJ0g&gsr=CijSDiUKIwoddG9wc2VsbGluZ19wYWlkX0VOVEVSVEFJTk1FTlQQBxgD:S:ANO1ljILXwg',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9FVkVOVFMQBxgD:S:ANO1ljIri5g&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0VWRU5UUxAHGAM%3D:S:ANO1ljL2Xvw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0VWRU5UUxAHGAM%3D:S:ANO1ljJI72c&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfRVZFTlRTEAcYAw%3D%3D:S:ANO1ljJpzdw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0VWRU5UUxAHGAM%3D:S:ANO1ljJqmyk&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfRVZFTlRTEAcYAw%3D%3D:S:ANO1ljIdwnQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9FVkVOVFMQBxgD:S:ANO1ljJ_Cp4&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0VWRU5UUxAHGAM%3D:S:ANO1ljJpVag',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcHNlbGxpbmdfZnJlZV9GSU5BTkNFEAcYAw%3D%3D:S:ANO1ljIqydA&gsr=CiLSDh8KHQoXdG9wc2VsbGluZ19mcmVlX0ZJTkFOQ0UQBxgD:S:ANO1ljJp7BU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4bChkKE3RvcGdyb3NzaW5nX0ZJTkFOQ0UQBxgD:S:ANO1ljLKbEY&gsr=Ch7SDhsKGQoTdG9wZ3Jvc3NpbmdfRklOQU5DRRAHGAM%3D:S:ANO1ljKBnkw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFm1vdmVyc19zaGFrZXJzX0ZJTkFOQ0UQBxgD:S:ANO1ljI3ap4&gsr=CiHSDh4KHAoWbW92ZXJzX3NoYWtlcnNfRklOQU5DRRAHGAM%3D:S:ANO1ljKiL98',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcHNlbGxpbmdfcGFpZF9GSU5BTkNFEAcYAw%3D%3D:S:ANO1ljIVTMA&gsr=CiLSDh8KHQoXdG9wc2VsbGluZ19wYWlkX0ZJTkFOQ0UQBxgD:S:ANO1ljJ3m50',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9GT09EX0FORF9EUklOSxAHGAM%3D:S:ANO1ljJyvJo&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0ZPT0RfQU5EX0RSSU5LEAcYAw%3D%3D:S:ANO1ljLP8G8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcGdyb3NzaW5nX0ZPT0RfQU5EX0RSSU5LEAcYAw%3D%3D:S:ANO1ljI5z7o&gsr=CiXSDiIKIAoadG9wZ3Jvc3NpbmdfRk9PRF9BTkRfRFJJTksQBxgD:S:ANO1ljJRNk8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHW1vdmVyc19zaGFrZXJzX0ZPT0RfQU5EX0RSSU5LEAcYAw%3D%3D:S:ANO1ljJI9Pg&gsr=CijSDiUKIwodbW92ZXJzX3NoYWtlcnNfRk9PRF9BTkRfRFJJTksQBxgD:S:ANO1ljKPw2w',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfcGFpZF9GT09EX0FORF9EUklOSxAHGAM%3D:S:ANO1ljKe4ss&gsr=CinSDiYKJAoedG9wc2VsbGluZ19wYWlkX0ZPT0RfQU5EX0RSSU5LEAcYAw%3D%3D:S:ANO1ljIbezM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfZnJlZV9IRUFMVEhfQU5EX0ZJVE5FU1MQBxgD:S:ANO1ljI8QpE&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19mcmVlX0hFQUxUSF9BTkRfRklUTkVTUxAHGAM%3D:S:ANO1ljImbKo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcGdyb3NzaW5nX0hFQUxUSF9BTkRfRklUTkVTUxAHGAM%3D:S:ANO1ljKG1qc&gsr=CinSDiYKJAoedG9wZ3Jvc3NpbmdfSEVBTFRIX0FORF9GSVRORVNTEAcYAw%3D%3D:S:ANO1ljJhKSc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIW1vdmVyc19zaGFrZXJzX0hFQUxUSF9BTkRfRklUTkVTUxAHGAM%3D:S:ANO1ljJGovk&gsr=CizSDikKJwohbW92ZXJzX3NoYWtlcnNfSEVBTFRIX0FORF9GSVRORVNTEAcYAw%3D%3D:S:ANO1ljJ2owY',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfcGFpZF9IRUFMVEhfQU5EX0ZJVE5FU1MQBxgD:S:ANO1ljKi9dU&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19wYWlkX0hFQUxUSF9BTkRfRklUTkVTUxAHGAM%3D:S:ANO1ljL8Vqc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9IT1VTRV9BTkRfSE9NRRAHGAM%3D:S:ANO1ljLJDPY&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0hPVVNFX0FORF9IT01FEAcYAw%3D%3D:S:ANO1ljIQlD0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcGdyb3NzaW5nX0hPVVNFX0FORF9IT01FEAcYAw%3D%3D:S:ANO1ljL1Mkc&gsr=CiXSDiIKIAoadG9wZ3Jvc3NpbmdfSE9VU0VfQU5EX0hPTUUQBxgD:S:ANO1ljKjMN4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHW1vdmVyc19zaGFrZXJzX0hPVVNFX0FORF9IT01FEAcYAw%3D%3D:S:ANO1ljLnVns&gsr=CijSDiUKIwodbW92ZXJzX3NoYWtlcnNfSE9VU0VfQU5EX0hPTUUQBxgD:S:ANO1ljKkFtw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfcGFpZF9IT1VTRV9BTkRfSE9NRRAHGAM%3D:S:ANO1ljIf01Y&gsr=CinSDiYKJAoedG9wc2VsbGluZ19wYWlkX0hPVVNFX0FORF9IT01FEAcYAw%3D%3D:S:ANO1ljI0VpM',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfZnJlZV9MSUJSQVJJRVNfQU5EX0RFTU8QBxgD:S:ANO1ljJDMDc&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19mcmVlX0xJQlJBUklFU19BTkRfREVNTxAHGAM%3D:S:ANO1ljLUmPI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcGdyb3NzaW5nX0xJQlJBUklFU19BTkRfREVNTxAHGAM%3D:S:ANO1ljLj_xc&gsr=CinSDiYKJAoedG9wZ3Jvc3NpbmdfTElCUkFSSUVTX0FORF9ERU1PEAcYAw%3D%3D:S:ANO1ljId31Q',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIW1vdmVyc19zaGFrZXJzX0xJQlJBUklFU19BTkRfREVNTxAHGAM%3D:S:ANO1ljI3GqI&gsr=CizSDikKJwohbW92ZXJzX3NoYWtlcnNfTElCUkFSSUVTX0FORF9ERU1PEAcYAw%3D%3D:S:ANO1ljImztk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfcGFpZF9MSUJSQVJJRVNfQU5EX0RFTU8QBxgD:S:ANO1ljIKufI&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19wYWlkX0xJQlJBUklFU19BTkRfREVNTxAHGAM%3D:S:ANO1ljJ4j-c',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfZnJlZV9MSUZFU1RZTEUQBxgD:S:ANO1ljLJG7Q&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19mcmVlX0xJRkVTVFlMRRAHGAM%3D:S:ANO1ljLRgKA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFXRvcGdyb3NzaW5nX0xJRkVTVFlMRRAHGAM%3D:S:ANO1ljIK1jQ&gsr=CiDSDh0KGwoVdG9wZ3Jvc3NpbmdfTElGRVNUWUxFEAcYAw%3D%3D:S:ANO1ljLKS14',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGG1vdmVyc19zaGFrZXJzX0xJRkVTVFlMRRAHGAM%3D:S:ANO1ljJSjTQ&gsr=CiPSDiAKHgoYbW92ZXJzX3NoYWtlcnNfTElGRVNUWUxFEAcYAw%3D%3D:S:ANO1ljK7Olk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfcGFpZF9MSUZFU1RZTEUQBxgD:S:ANO1ljJezOA&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19wYWlkX0xJRkVTVFlMRRAHGAM%3D:S:ANO1ljL9KYw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfZnJlZV9NQVBTX0FORF9OQVZJR0FUSU9OEAcYAw%3D%3D:S:ANO1ljKX-Y4&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19mcmVlX01BUFNfQU5EX05BVklHQVRJT04QBxgD:S:ANO1ljI9GbI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcGdyb3NzaW5nX01BUFNfQU5EX05BVklHQVRJT04QBxgD:S:ANO1ljJIA-4&gsr=CirSDicKJQofdG9wZ3Jvc3NpbmdfTUFQU19BTkRfTkFWSUdBVElPThAHGAM%3D:S:ANO1ljIrYq8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKIm1vdmVyc19zaGFrZXJzX01BUFNfQU5EX05BVklHQVRJT04QBxgD:S:ANO1ljL_wE4&gsr=Ci3SDioKKAoibW92ZXJzX3NoYWtlcnNfTUFQU19BTkRfTkFWSUdBVElPThAHGAM%3D:S:ANO1ljIZcnI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfcGFpZF9NQVBTX0FORF9OQVZJR0FUSU9OEAcYAw%3D%3D:S:ANO1ljJSUyY&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19wYWlkX01BUFNfQU5EX05BVklHQVRJT04QBxgD:S:ANO1ljK63Nc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcHNlbGxpbmdfZnJlZV9NRURJQ0FMEAcYAw%3D%3D:S:ANO1ljKb330&gsr=CiLSDh8KHQoXdG9wc2VsbGluZ19mcmVlX01FRElDQUwQBxgD:S:ANO1ljKyYVU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4bChkKE3RvcGdyb3NzaW5nX01FRElDQUwQBxgD:S:ANO1ljL-pGs&gsr=Ch7SDhsKGQoTdG9wZ3Jvc3NpbmdfTUVESUNBTBAHGAM%3D:S:ANO1ljIpVC0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFm1vdmVyc19zaGFrZXJzX01FRElDQUwQBxgD:S:ANO1ljLvUvs&gsr=CiHSDh4KHAoWbW92ZXJzX3NoYWtlcnNfTUVESUNBTBAHGAM%3D:S:ANO1ljKx8Eg',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcHNlbGxpbmdfcGFpZF9NRURJQ0FMEAcYAw%3D%3D:S:ANO1ljL-SAg&gsr=CiLSDh8KHQoXdG9wc2VsbGluZ19wYWlkX01FRElDQUwQBxgD:S:ANO1ljLkETk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfZnJlZV9NVVNJQ19BTkRfQVVESU8QBxgD:S:ANO1ljJSp24&gsr=CirSDicKJQofdG9wc2VsbGluZ19mcmVlX01VU0lDX0FORF9BVURJTxAHGAM%3D:S:ANO1ljIDvvE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcGdyb3NzaW5nX01VU0lDX0FORF9BVURJTxAHGAM%3D:S:ANO1ljKRh0M&gsr=CibSDiMKIQobdG9wZ3Jvc3NpbmdfTVVTSUNfQU5EX0FVRElPEAcYAw%3D%3D:S:ANO1ljLjcRw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHm1vdmVyc19zaGFrZXJzX01VU0lDX0FORF9BVURJTxAHGAM%3D:S:ANO1ljKOqas&gsr=CinSDiYKJAoebW92ZXJzX3NoYWtlcnNfTVVTSUNfQU5EX0FVRElPEAcYAw%3D%3D:S:ANO1ljIPqP0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfcGFpZF9NVVNJQ19BTkRfQVVESU8QBxgD:S:ANO1ljKffcs&gsr=CirSDicKJQofdG9wc2VsbGluZ19wYWlkX01VU0lDX0FORF9BVURJTxAHGAM%3D:S:ANO1ljI8jRo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfZnJlZV9ORVdTX0FORF9NQUdBWklORVMQBxgD:S:ANO1ljLkZUE&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19mcmVlX05FV1NfQU5EX01BR0FaSU5FUxAHGAM%3D:S:ANO1ljLuezs',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcGdyb3NzaW5nX05FV1NfQU5EX01BR0FaSU5FUxAHGAM%3D:S:ANO1ljIOfRU&gsr=CinSDiYKJAoedG9wZ3Jvc3NpbmdfTkVXU19BTkRfTUFHQVpJTkVTEAcYAw%3D%3D:S:ANO1ljKPbuE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIW1vdmVyc19zaGFrZXJzX05FV1NfQU5EX01BR0FaSU5FUxAHGAM%3D:S:ANO1ljK2BfY&gsr=CizSDikKJwohbW92ZXJzX3NoYWtlcnNfTkVXU19BTkRfTUFHQVpJTkVTEAcYAw%3D%3D:S:ANO1ljKkTgI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKInRvcHNlbGxpbmdfcGFpZF9ORVdTX0FORF9NQUdBWklORVMQBxgD:S:ANO1ljIeAhc&gsr=Ci3SDioKKAoidG9wc2VsbGluZ19wYWlkX05FV1NfQU5EX01BR0FaSU5FUxAHGAM%3D:S:ANO1ljLmoGU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfZnJlZV9QQVJFTlRJTkcQBxgD:S:ANO1ljI8w1M&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19mcmVlX1BBUkVOVElORxAHGAM%3D:S:ANO1ljK7gT4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFXRvcGdyb3NzaW5nX1BBUkVOVElORxAHGAM%3D:S:ANO1ljJ0QcQ&gsr=CiDSDh0KGwoVdG9wZ3Jvc3NpbmdfUEFSRU5USU5HEAcYAw%3D%3D:S:ANO1ljLBdB0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGG1vdmVyc19zaGFrZXJzX1BBUkVOVElORxAHGAM%3D:S:ANO1ljLJhho&gsr=CiPSDiAKHgoYbW92ZXJzX3NoYWtlcnNfUEFSRU5USU5HEAcYAw%3D%3D:S:ANO1ljLhAyw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcHNlbGxpbmdfcGFpZF9QQVJFTlRJTkcQBxgD:S:ANO1ljLGguM&gsr=CiTSDiEKHwoZdG9wc2VsbGluZ19wYWlkX1BBUkVOVElORxAHGAM%3D:S:ANO1ljJo50E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfZnJlZV9QRVJTT05BTElaQVRJT04QBxgD:S:ANO1ljJG8bM&gsr=CirSDicKJQofdG9wc2VsbGluZ19mcmVlX1BFUlNPTkFMSVpBVElPThAHGAM%3D:S:ANO1ljL79WA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcGdyb3NzaW5nX1BFUlNPTkFMSVpBVElPThAHGAM%3D:S:ANO1ljKWuOs&gsr=CibSDiMKIQobdG9wZ3Jvc3NpbmdfUEVSU09OQUxJWkFUSU9OEAcYAw%3D%3D:S:ANO1ljI86DI',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHm1vdmVyc19zaGFrZXJzX1BFUlNPTkFMSVpBVElPThAHGAM%3D:S:ANO1ljKpxmg&gsr=CinSDiYKJAoebW92ZXJzX3NoYWtlcnNfUEVSU09OQUxJWkFUSU9OEAcYAw%3D%3D:S:ANO1ljICpKE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcHNlbGxpbmdfcGFpZF9QRVJTT05BTElaQVRJT04QBxgD:S:ANO1ljLgkwE&gsr=CirSDicKJQofdG9wc2VsbGluZ19wYWlkX1BFUlNPTkFMSVpBVElPThAHGAM%3D:S:ANO1ljJwYBU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9QSE9UT0dSQVBIWRAHGAM%3D:S:ANO1ljI2KAA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX1BIT1RPR1JBUEhZEAcYAw%3D%3D:S:ANO1ljLbsoc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX1BIT1RPR1JBUEhZEAcYAw%3D%3D:S:ANO1ljJUavw&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfUEhPVE9HUkFQSFkQBxgD:S:ANO1ljLzymE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGm1vdmVyc19zaGFrZXJzX1BIT1RPR1JBUEhZEAcYAw%3D%3D:S:ANO1ljKwgi8&gsr=CiXSDiIKIAoabW92ZXJzX3NoYWtlcnNfUEhPVE9HUkFQSFkQBxgD:S:ANO1ljJSIJ8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfcGFpZF9QSE9UT0dSQVBIWRAHGAM%3D:S:ANO1ljJpURY&gsr=CibSDiMKIQobdG9wc2VsbGluZ19wYWlkX1BIT1RPR1JBUEhZEAcYAw%3D%3D:S:ANO1ljIS7Hc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHHRvcHNlbGxpbmdfZnJlZV9QUk9EVUNUSVZJVFkQBxgD:S:ANO1ljL0j68&gsr=CifSDiQKIgocdG9wc2VsbGluZ19mcmVlX1BST0RVQ1RJVklUWRAHGAM%3D:S:ANO1ljJNyCo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcGdyb3NzaW5nX1BST0RVQ1RJVklUWRAHGAM%3D:S:ANO1ljIgHiM&gsr=CiPSDiAKHgoYdG9wZ3Jvc3NpbmdfUFJPRFVDVElWSVRZEAcYAw%3D%3D:S:ANO1ljLDCMk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG21vdmVyc19zaGFrZXJzX1BST0RVQ1RJVklUWRAHGAM%3D:S:ANO1ljJBoK8&gsr=CibSDiMKIQobbW92ZXJzX3NoYWtlcnNfUFJPRFVDVElWSVRZEAcYAw%3D%3D:S:ANO1ljIrYpg',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHHRvcHNlbGxpbmdfcGFpZF9QUk9EVUNUSVZJVFkQBxgD:S:ANO1ljJM_WQ&gsr=CifSDiQKIgocdG9wc2VsbGluZ19wYWlkX1BST0RVQ1RJVklUWRAHGAM%3D:S:ANO1ljK71YA',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfZnJlZV9TSE9QUElORxAHGAM%3D:S:ANO1ljIm-qs&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19mcmVlX1NIT1BQSU5HEAcYAw%3D%3D:S:ANO1ljIc-1Q',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcGdyb3NzaW5nX1NIT1BQSU5HEAcYAw%3D%3D:S:ANO1ljJRRXk&gsr=Ch_SDhwKGgoUdG9wZ3Jvc3NpbmdfU0hPUFBJTkcQBxgD:S:ANO1ljKJ3Iw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF21vdmVyc19zaGFrZXJzX1NIT1BQSU5HEAcYAw%3D%3D:S:ANO1ljIVCWA&gsr=CiLSDh8KHQoXbW92ZXJzX3NoYWtlcnNfU0hPUFBJTkcQBxgD:S:ANO1ljL_N9I',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfcGFpZF9TSE9QUElORxAHGAM%3D:S:ANO1ljKieJc&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19wYWlkX1NIT1BQSU5HEAcYAw%3D%3D:S:ANO1ljKYoE4'
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
        yield apps
        print(main_list)




   