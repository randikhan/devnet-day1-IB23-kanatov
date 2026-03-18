# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Kanatov Erkhan
- Group: IB-23-5B
- Token: D1-IB-23-5b-08-4B6A
- Repo: 

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots:
  - GET /books
  - POST /loginViaBasic
- Postman screenshots:
  - Collection `Day3-Library-IB-23-5B-08`
  - POST /books с X-API-KEY
  - GET /books?includeISBN=true&sortBy=author
- Python run screenshot:
  - `python src/day3_library_lab.py --count 100` выполнен успешно

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
python src/day3_library_lab.py --count 100