
# OneunionGPT

## Структура проекта

```
myproject/ 
    ├── app/ │
        ├── main.py │ 
        ├── models.py │
    ├── requirements.txt 
    └── .env
```

## API 

#### Отправка

```http
  POST /generate/
```

| Parameter | Type     | 
| :-------- | :------- | 
| `descripton` | `string` |

```json
{
    "description": "Описание вашего продукта"
}
```

#### Получение

| Parameter | Type     | 
| :-------- | :------- | 
| `result`      | `string` | 

```json
{
    "result": "Сгенерированное маркетинговое описание"
}
```


## Пример использования

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Text Generator</title>
</head>
<body>
    <h1>Marketing Text Generator</h1>
    <textarea id="description" placeholder="Введите описание продукта"></textarea>
    <button onclick="generateText()">Сгенерировать</button>
    <h2>Результат:</h2>
    <p id="result"></p>

    <script>
        async function generateText() {
            const description = document.getElementById('description').value;
            const response = await fetch('http://127.0.0.1:8000/generate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ description: description })
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('result').innerText = data.result;
            } else {
                document.getElementById('result').innerText = 'Ошибка при генерации текста';
            }
        }
    </script>
</body>
</html>
```

