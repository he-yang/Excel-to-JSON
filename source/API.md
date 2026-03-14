# 5. API (Excel to JSON by HTTPS POST request)

[中文](https://excel-to-json.wtsolutions.cn/zh-cn/latest/API.html)

Excel to JSON by WTSolutions is a series of tools which can convert Excel to JSON, both Flat and Nested JSON can be converted. It offer a full-scenario solution for "Converting Excel to JSON", including Excel add-ins, web applications, open APIs, and enterprise-grade MCP tools:

* [Web App: Convert Excel to JSON directly in Web Browser.](WebApp.md)
* [Excel add-in: Convert Excel to JSON in Excel, works with Excel environment seamlessly.](ExcelAddIn.md)
* [WPS add-in: Convert WPS workbook to JSON in WPS, works with WPS environment seamlessly.](WPSAddIn.md)
* <mark>API: Convert Excel to JSON by HTTPS POST request.</mark> (<-- You are here.)
* [MCP Service: Convert Excel to JSON by AI Model MCP SSE/StreamableHTTP request.](MCP.md)

## 5.1 Requirements

HTTPS post request tool, e.g. Postman, Curl, Python Requests, Javascript fetch, etc.
Make sure you properly handle CORS issues by setting up CORS headers.

## 5.2 Access

Send `POST` request to access point `https://mcp.wtsolutions.cn/excel-to-json-api` with required parameters described below in usage section. 

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8772217510669640"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-8772217510669640"
     data-ad-slot="2653271427"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 5.3 Usage

### 5.3.1 Request Format

The API accepts POST requests with a `application/json` body containing one of the following parameter:

| Parameter | Type   | Required | Description                                                                 |
|-----------|--------|----------|-----------------------------------------------------------------------------|
| data      | string | No       | Tab-separated or comma-separated text data with at least two rows (header row + data row). Either 'data' or 'url' must be provided |
| url       | string | No       | URL pointing to an Excel or CSV file. Either 'data' or 'url' must be provided |
| options   | object | Yes       | Optional configuration object for customizing the conversion process        |

> Note: 
> - Provide either `data` or `url`, not both.
> - `options` is mandatory if you want to use custom conversion settings. 
> - By default, max 6 rows of data conversion is performed. To convert more rows, a valid Pro Code is required.

#### Requirements on data and url

When sending `data`
- Input data must be tab-separated (Excel) or comma-separated (CSV) text with at least two rows (header row + data row) or two columns (header column + data column) depends on your "header" setting in options parameter.
  1. The first row or column will be considered as "header" row/column, and this API will use it as column names, subsequently JSON keys.
  2. The following rows or columns will be considered as "data" rows/columns, and this API will use them as JSON values.

When sending `url`
- Each sheet of the Excel file should contain at least two rows or columns (header row/column + data row/column).
  1. The first row or column will be considered as "header" row/column, and this API will use it as column names, subsequently JSON keys.
  2. The following rows or columns will be considered as "data" rows/columns, and this API will use them as JSON values.
- This Excel file should be in '.xlsx' format.
- Each sheet of the Excel file will be converted to a JSON object.
- Each JSON object will have 'sheetName' (string) and 'data' properties.
- Each JSON object in 'data' array will have properties corresponding to header names.
- Each JSON object in 'data' array will have values corresponding to cell values.


### 5.3.2 Options Object
The optional `options` object can contain the following properties:

| Property             | Type   | Default   | Description                                                                 |
|----------------------|--------|-----------|-----------------------------------------------------------------------------|
| [proCode](profeatures.md#pro-code)              | string | ""        | Pro Code for Pro Version Excel to JSON subscription. |
| [jsonMode](profeatures.md#conversion-mode)             | string | "flat"    | Format mode for JSON output: "nested", or "flat"                   |
| [header](profeatures.md#select-header-row-or-column)               | string | "row"     | Specifies which row/column to use as headers: "row" (first row) or "column" (first column) |
| [delimiter](profeatures.md#nested-json-key-delimeter)            | string | "."       | Delimiter character for nested JSON keys when using `jsonMode`: "nested", acceptable delimiters are ".", "_", "__", "/". |
| [emptyCell](profeatures.md#output-format-for-empty-cell)            | string | "emptyString" | Handling of empty cells: "emptyString", "null", or "exclude"               |
| [booleanFormat](profeatures.md#output-format-for-boolean-values)        | string | "trueFalse" | Format for boolean values: "trueFalse", "10", or "string"                   |
| [jsonFormat](profeatures.md#output-format-for-json)           | string | "arrayOfObject" | Overall JSON output format: "arrayOfObject" or "2DArray"                    |
| [singleObjectFormat](profeatures.md#output-format-for-single-object-json)   | string | "array"   | Format when result has only one object: "array" (keep as array) or "object" (return as single object) |

> Note:
> - `delimiter` works only when `jsonMode` is "nested".
> - `singleObjectFormat` works only when `jsonFormat` is "arrayOfObject". 
> - `jsonFormat` as "2DArray" works only when `jsonMode` is "flat".
> - `proCode` is mandatory. Without a valid Pro Code, the API handle max. 6 rows of data.
> - Detailed conversion rules can be found in [Conversion Features](profeatures.md).

### 5.3.3 Response Format
The API returns a JSON object with the following structure:

| Field   | Type    | Description                                                                 |
|---------|---------|-----------------------------------------------------------------------------|
| isError | boolean | Indicates if there was an error processing the request                      |
| msg     | string  | 'success' or error description                                              |
| data    | string  | Converted data as array of sheet objects if using URL, string if using direct data, '' if there was an error.|


### 5.3.4 Examples 

#### Example Request with 'data'

Original data:

| id | student.name | student.familyname | student.age |
|----|--------------|--------------------|-------------|
| 1  | Meimei       | Han                | 12          |
| 2  | Lily         | Jaskson            | 15          |
| 3  | Elon         | Mask               | 18          |

Request 1:

```json
{
     "data": "id\tstudent.name\tstudent.familyname\tstudent.age\n1\tMeimei\tHan\t12\n2\tLily\tJaskson\t15\n3\tElon\tMask\t18",
     "options": {
         "proCode": "proCode(please input your proCode)",
         "jsonMode": "nested",
         "delimiter": "."
     }
}
```
Response 1:
```json
{
	"isError": false,
	"msg": "success",
	"data": "[{\"id\":1,\"student\":{\"name\":\"Meimei\",\"familyname\":\"Han\",\"age\":12}},{\"id\":2,\"student\":{\"name\":\"Lily\",\"familyname\":\"Jaskson\",\"age\":15}},{\"id\":3,\"student\":{\"name\":\"Elon\",\"familyname\":\"Mask\",\"age\":18}}]"
}
```

Request 2:
```json
{
     "data": "id\tstudent.name\tstudent.familyname\tstudent.age\n1\tMeimei\tHan\t12\n2\tLily\tJaskson\t15\n3\tElon\tMask\t18",
     "options": {
         "proCode": "proCode(please input your proCode)",
         "jsonMode": "flat",
         "jsonFormat": "2DArray"
     }
}
```


Response 2:
```json
{
	"isError": false,
	"msg": "success",
	"data": "[[\"id\",\"student.name\",\"student.familyname\",\"student.age\"],[1,\"Meimei\",\"Han\",12],[2,\"Lily\",\"Jaskson\",15],[3,\"Elon\",\"Mask\",18]]"
}
```

#### Example Success Response with 'url' (Multi-sheet Excel)

Origin Excel Data in `Sheet1`:

| Name       | Age | IsStudent |
|------------|-----|-----------|
| John Doe   | 25  | false     |
| Jane Smith | 30  | true      |

Origin Excel Data in `Sheet2`:

| ID | Value   |
|----|---------|
| 1  | Example |


Request:

```json
{
     "url": "https://tools.wtsolutions.cn/example.xlsx",
     "options": {
         "proCode": "proCode(please input your proCode)",
         "booleanFormat": "10",
         "jsonFormat": "arrayOfObject",
         "singleObjectFormat": "object"
     }
}
```

Response:

```json
{
	"isError": false,
	"msg": "success",
	"data": "[{\"sheetName\":\"Sheet1\",\"data\":[{\"Name\":\"John Doe\",\"Age\":25,\"IsStudent\":0},{\"Name\":\"Jane Smith\",\"Age\":30,\"IsStudent\":1}]},{\"sheetName\":\"Sheet2\",\"data\":{\"ID\":1,\"Value\":\"Example\"}}]"
}
```

#### Example Error Response
```json
{
     "isError": true,
     "msg": "At least 2 rows are required in Excel Data",
     "data": ""
}
```

### 5.3.5 Data Type Handling
This API automatically detects and converts different data types, while users can customize the conversion rules by providing an 'options' object in the request body as described.
- **Numbers**: Converted to numeric values
- **Booleans**: Recognizes 'true'/'false' (case-insensitive) and converts to boolean values
- **Dates**: Detects various date formats and converts them appropriately
- **Strings**: Treated as string values
- **Empty values**: Represented as empty strings

## 5.4 Error Handling
The API returns descriptive error messages for common issues:
- `Excel Data Format Invalid`: When input data is not tab-separated or comma-separated
- `At least 2 rows are required`: When input data has fewer than 2 rows
- `Both data and url received`: When both 'data' and 'url' parameters are provided
- `Network Error when fetching file`: When there's an error downloading the file from the provided URL
- `File not found`: When the file at the provided URL cannot be found
- `Blank/Null/Empty cells in the first row not allowed`: When header row contains empty cells
- `Server Internal Error`: When an unexpected error occurs
- `Max 6 rows handled, upgrade to Pro to handle more rows`: When a valid Pro Code is not provided, the API handles max. 6 rows of data