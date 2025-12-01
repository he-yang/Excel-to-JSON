# 7. Excel Data and Conversion Settings

[中文](https://excel-to-json.wtsolutions.cn/zh-cn/latest/profeatures.html)

Excel to JSON by WTSolutions offers a set of rules of conversion that enhance the functionality of the tools. 
These rules marked as [Pro Feature](pricing.md) are only available to users who have subscribed the tools.

## 7.1 Excel Data

### DataSource
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

There are several ways for you to input Excel data to Excel to JSON Web App and Excel add-in, or WPS workbook data to WPS add-in:

* Web App: `Load Excel to JSON in web browser`
    *  Copy and Paste your Excel data in the text area
    *  You can copy and paste your Excel data from Excel, Google Sheets, or any other Excel-compatible software, data are seperated by Tab
    *  You can also copy and paste comma seperated CSV data
* Excel Add-in: `Side-load Excel to JSON in Excel`: 
    * Select your data directly from Excel worksheet using your mouse or keyboard.
    * Or, let Excel to JSON to convert all visible sheets from Excel. [Pro Feature](pricing.md)
    * Or, let Excel to JSON to convert all sheets from Excel. [Pro Feature](pricing.md)
* WPS Add-in: `Side-load WPS sheet to JSON in WPS`: 
    * Select your data directly from WPS worksheet using your mouse or keyboard



## 7.2 Conversion Settings

### Select Header Row or Column
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

You can specify:
- First Row as header
    - The first row will be considered as "header" row, and will be used as column names, subsequently JSON keys.
    - The following rows will be considered as "data" rows, and this will be treated as JSON values.
- First Column as header [Pro Feature](pricing.md)
    - The first column will be considered as "header" column, and will be used as JSON keys, subsequently JSON values.
    - The columns on the right will be considered as "data" columns, and this will be treated as JSON values.

### Conversion Mode
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

The Conversion Mode specifies how to convert Excel data to JSON. The default mode is `Flat`.

* `flat`: Converts Excel data to JSON in a flat structure.
* `nested`: Converts Excel data to JSON in a nested structure. [Pro Feature](pricing.md)

### Nested JSON Key Delimeter
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

The Nested JSON Key Delimeter specifies how to separate nested keys in Nested JSON Mode. The default delimiter is a dot (.).

You can also use other delimiters like:
- `Dot (.)` or `"."`
- `Underscore (_)` or `"_"` [Pro Feature](pricing.md)
- `Double Underscore (__)` or `"__"` [Pro Feature](pricing.md)
- `Forward Slash(/)` or `"/"` [Pro Feature](pricing.md)

For example, using underscore (_) as delimiter:

|id|<mark>student_name</mark>|student_familyname|student_age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

Using Dot(.) as delimiter:
|id|<mark>student.name</mark>|student.familyname|student.age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

Using Forward Slash(/) as delimiter:
|id|<mark>student/name</mark>|student/familyname|student/age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

Will generate:

> Using Nested JSON mode with delimiter "_", ".", "/" respectively.

```json
[{
    "id": 1,
    "student": {
        "name": "Meimei",
        "familyname": "Han",
        "age": 12
    }
}, {
    "id": 2,
    "student": {
        "name": "Lily",
        "familyname": "Jaskson",
        "age": 15
    }
}]
```
### Output Format for Empty Cell
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

The Empty Cell option handles empty cells in Excel/WPS Workbook with three approaches:

1. `empty string ""` or `"emptyString"`: Converts empty cells to empty strings `""`
2. `JSON null` or `"null"`: Converts empty cells to `null` [Pro Feature](pricing.md)
3. `not include in JSON` or `"exclude"`: Excludes empty cells from JSON [Pro Feature](pricing.md). This option is not available in 2DArray format output JSON.

**Example Excel sheet**

|Name|Age|Company|
|---|---|---|
|David|27|WTSolutions|
|Ton||Microsoft|

> Using Empty Cell = "null"

```json
[{
    "Name": "David",
    "Age": 27,
    "Company": "WTSolutions"
}, {
    "Name": "Ton",
    // see here
    "Age": null,
    "Company": "Microsoft"
}]
```
> Using Empty Cell = "empty string"
```json
[{
    "Name": "David",
    "Age": 27,
    "Company": "WTSolutions"
}, {
    "Name": "Ton",
    // see here
    "Age": "",
    "Company": "Microsoft"
}]
```
> Using Empty Cell = "not include in JSON"
```json
    "Name": "David",
    "Age": 27,
    "Company": "WTSolutions"
}, {
    "Name": "Ton",
    // see here
    "Company": "Microsoft"
}]
```

### Output Format for Boolean Values
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

The Boolean Format specifies how to convert boolean values in Excel/WPS Workbook:

1. `JSON true/false` or `"trueFalse"`: Converts to JSON boolean values (`true` or `false`)
2. `String "true"/"false"` or `"string"`: Converts to strings (`"true"` or `"false"`) [Pro Feature](pricing.md)
3. `Number 1/0` or `"10"`: Converts to numbers (`1` for `TRUE`, `0` for `FALSE`) [Pro Feature](pricing.md)

**Example Excel sheet**

|Name|IsStudent|IsEmployed|
|---|---|---|
|David|TRUE|FALSE|
|Ton|FALSE|TRUE|

> Using Boolean Format = "JSON true/false"

```json
[{
    "Name": "David",
    // see here
    "IsStudent": true,
    "IsEmployed": false
}, {
    "Name": "Ton",
    "IsStudent": false,
    "IsEmployed": true
}]
```
> Using Boolean Format = "String "true"/"false""
```json
[{
    "Name": "David",
    // see here
    "IsStudent": "true",
    "IsEmployed": "false"
}, {
    "Name": "Ton",
    "IsStudent": "false",
    "IsEmployed": "true"
}]
```
> Using Boolean Format = "Number 1/0"
```json
[{
    "Name": "David",
    // see here
    "IsStudent": 1,
    "IsEmployed": 0
}, {
    "Name": "Ton",
    "IsStudent": 0,
    "IsEmployed": 1
}]
```

### Output Format for Date Format values
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|❌|✅|✅|❌|❌|

This feature allows you to convert date values in Excel/WPS Workbook to a specific format, such as ISO 8601 or number of days from 1900-01-01. It is not avalible when you load Excel to JSON in web browser. If you want to convert date values in Excel/WPS Workbook to a specific format, you can sideload Excel to JSON in Excel/WPS application.

The Date Format specifies how to convert date values in Excel/WPS Workbook:

1. `Number of Days from 1900-01-01`: Converts to number of days since 1900-01-01
2. `String, ISO 8601 (YYYY-MM-DDTHH:mm:ssZ)`: Converts to ISO 8601 formatted string [Pro Feature](pricing.md)


> <mark> Note: The Date Format feature only work, if you add $date$ as suffix in your Excel/WPS Workbook Datasheet first row. Refer to the subsequent example header row. </mark>
> Note: Excel can not render Dates before 1900-01-01 as Date format, so you may find that cell be interpreted as String format.
> For instance, if you want to convert the Birthday column to ISO8601 format, you should add $date$ as surfix in the column header, see example below.

**Example Excel sheet**

|Name|<mark>Birthday$date$</mark>|
|---|---|
|David|1900-01-01|
|Ton|1995-05-15|

> Using Date Format = "Number of Days from 1900-01-01"

```json
[{
    "Name": "David",
    "Birthday": 1
}, {
    "Name": "Ton",
    // see here
    "Birthday": 34834
}]
```
> Using Date Format = "String, ISO 8601 (> Using Date Format = "String, ISO 8601 (ssZ)"
```json
[{
    "Name": "David",
    "Birthday": "1900-01-01T00:00:00.000Z"
}, {
    "Name": "Ton",
    // see here
    "Birthday": "1995-05-15T00:00:00.000Z"
}]
```

### Output Format for JSON
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

There are two options for you to present output JSON:
1. `Array of object` or `"arrayOfObject"`
2. `2D Array` or `"2DArray"` [Pro Feature](pricing.md)

**Example Excel sheet**

|Name|Age|Company|
|---|---|---|
|David|27|WTSolutions|
|Ton|25|Microsoft|

> Using "Array of object" option.

```json
[{
    "Name": "David",
    "Age": 27,
    "Company": "WTSolutions"        
},
{
    "Name": "Ton",
    "Age": 25,
    "Company": "Microsoft"  
}
]
```
> Using "2D Array" option.
```json
[
    ["Name", "Age", "Company"]
    ["David", 27, "WTSolutions"],
    ["Ton", 25, "Microsoft"]
]
```

### Output Format for Single Object JSON
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|✅|❌|

The option specifies how to perserve single object JSON, when there is only one object in the converted JSON:

1. `Array []` or `"array"`: Converts to an array of one object
2. `Object {}` or `"object"`: Converts to one object [Pro Feature](pricing.md)


> Note: The feature only work, when there is only one object in the converted JSON, and the output format for JSON is Array of Object.

**Example Excel sheet**

|Name|Age|
|---|---|
|David|20|

> Using "Array []"

```json
[{
    "Name": "David",
    "Age": 20
}]
```
> Using "Object {}"
```json
{
    "Name": "David",
    "Age": 20
}
```

### Filename at SaveAs
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[WPS Add-in](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

The Save As Filename feature allows you to specify a custom filename for your JSON output file，when you click on the "Save As" botton after the conversion. When you enter a filename in this field, the converted JSON data will be saved with your specified name instead of the default name(excel-to-json.json).

**Filename Requirements:**
- Maximum length: 200 characters (excluding extension)
- File extension will be automatically set to .json
- Cannot start or end with dots (.) or spaces
- Cannot use Windows reserved names (e.g., CON, PRN, AUX, etc.)
- Cannot contain the following characters: < > : \ / | ? *

**Example:**
- Valid filenames: data.json, my_data.json, export_2024.json
- Invalid filenames: .data.json, con.json, my:data.json

**Support Platforms:**
- Excel on Windows, yes
- Web version of Excel on Office.com or Onedrive, yes
- Excel for Mac, not supported
  - If you are a Mac user, you can use Web version of Excel on Office.com or Onedrive.

If you are sideloading Excel to JSON Excel add-in and, your Excel on Windows version is 1801 (Office 2019) or later. You can find two additional buttons, helping you get Workbook name and Worksheet name.

**Take Workbook Name**
- Click the "Take Workbook Name" button to automatically retrieve the name of the currently open Excel workbook.
- The workbook name will be displayed in the "Filename at SaveAs" input text box.

**Take Worksheet Name**
- Click the "Take Worksheet Name" button to automatically retrieve the name of the currently active worksheet.
- The worksheet name will be displayed in the "Filename at SaveAs" input text box.

## 7.3 No Ads

If you have a valid subscription to Excel-to-JSON, you will not see ads after a successful conversion with a valid Pro Code.

Starting from the next launch (you can shut down Excel-to-JSON and then start it again), Excel-to-JSON will no longer display ads. 

Ads will be displayed if you do not have a valid Pro Code, or if you do not have a valid subscription to Excel-to-JSON.

> Note, If you still see ads displayed from time to time, try to make a conversion with a valid Pro Code, then restart Excel-to-JSON.

## 7.4 More features

If you have subscribed, and would like to see more features, kindly please send us email at he.yang@wtsolutions.cn

## 7.5 Pro Code

Pro Code is the `email address` you used during the checkout process of the Excel-to-JSON add-in on Stripe or Paddle. This code is required to access pro features.

## 7.6 Aftersale services

You can contact us via email at he.yang@wtsolutions.cn for any questions or concerns. We will try our best to respond you within 24 hours, but not later than 72 hours. Please include your `Pro Code` in the email if your question is related to your subscription.
