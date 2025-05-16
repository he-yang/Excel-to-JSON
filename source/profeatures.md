# Pro Features

[中文](https://excel-to-json.wtsolutions.cn/zh-cn/latest/profeatures.html)

The Excel-to-JSON add-in offers a set of pro features that enhance the functionality of the add-in. These features are only available to users who have subscribed the add-in.

## Subscription

7 days free trial, then you will be charged monthly at one of the following rates for the Pro Features. You can cancel your subscription at any time before the 7th day, and you will not be charged:
- USD US$2.66 / month,
- CNY ¥19.90 / month,
- EUR €2.36 / month,
- HKD HK$21.80 / month
- Your local currency, if Stripe supports it.

Each Pro Code can offer 10 devices to access Pro Features.After the 7 day trial period, you may cancel your subscription at any time, which will take effect at the end of your current billing cycle.

Each Pro code is valid for both Excel-to-JSON and [JSON-to-Excel](https://json-to-excel.wtsolutions.cn/en/latest/) add-in provided by WTSolutions.

Subscribe through Stripe, here [https://buy.stripe.com/00gdQT2iz0Vp32E002](https://buy.stripe.com/00gdQT2iz0Vp32E002)
Payment method:
- Bank Card (Visa, Mastercard, American Express, JCB, 银联)
- Apple Pay (needs to open the above link using your Apple/IOS/Mac Device)
- Google Pay (needs to open the above link using your Google/Andriod Device)
- Link

For subscription terms, kindly refer to the [Terms of Use](termsofuse.md)

## Pro Code

Pro Code is the `email address` you used during the checkout process of the Excel-to-JSON add-in on Stripe. This code is required to access pro features.

## Nested Delimeter

The Nested Delimeter specifies how to separate nested keys in Nested JSON Mode. The default delimiter is a dot (.).

You can also use other delimiters like:
- Forward slash (/)
- Underscore (_) 
- Dot (.)

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
## Empty Cell

The Empty Cell option handles empty cells in Excel with three approaches:

1. `empty string ""`: Converts empty cells to empty strings `""`
2. `JSON null`: Converts empty cells to `null`
3. `not include in JSON`: Excludes empty cells from JSON

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

## Boolean Format

The Boolean Format specifies how to convert boolean values in Excel:

1. `JSON true/false`: Converts to JSON boolean values (`true` or `false`)
2. `String "true"/"false"`: Converts to strings (`"true"` or `"false"`)
3. `Number 1/0`: Converts to numbers (`1` for `TRUE`, `0` for `FALSE`)

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

## Date Format

The Date Format specifies how to convert date values in Excel:

1. `Number of Days from 1900-01-01`: Converts to number of days since 1900-01-01
2. `String, ISO 8601 (YYYY-MM-DDTHH:mm:ssZ)`: Converts to ISO 8601 formatted string

> <mark> Note: The Date Format feature only work, if you add $date$ as suffix in your Excel Datasheet first row. Refer to the subsequent example header row. </mark>
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

## Save As Filename

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


## More features

If you have subscribed, and would like to see more features, kindly please send us email at he.yang@wtsolutions.cn

## Aftersale services

You can contact us via email at he.yang@wtsolutions.cn for any questions or concerns. We will try our best to respond you within 24 hours, but not later than 72 hours. Please include your `Pro Code` in the email if your question is related to your subscription.
