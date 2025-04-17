# Excel-to-JSON

[![Documentation Status](https://readthedocs.org/projects/excel-to-json/badge/?version=latest)](http://excel-to-json.readthedocs.io/en/latest/?badge=latest)

[简体中文](https://github.com/he-yang/Excel-to-JSON-zh-CN)

Excel add-in converting excel to json

Excel-to-JSON is now available on Microsoft Appsource (formerly known as Office Store). https://store.office.com/app.aspx?assetid=WA104380263

## Documentation
[https://excel-to-json.wtsolutions.cn](https://excel-to-json.wtsolutions.cn)

## Get Started

Excel to JSON is a Microsoft Excel add-in which can convert Excel to JSON.

## Requirements
This add-in works with Excel 2013(or higher), Excel Online, Office 365, Excel for Mac.

## Get add-in
* Open a new datasheet in Excel 2013/2016 or higher, Excel Online or Office 365 etc.	
* **Insert** Tab or **Home** Tab> Add-ins.
* In the Add-ins search box, search for “Excel-to-JSON”. 
* Click the add-in to start it.
* You would see a "Excel-to-JSON" button added to your Excel **Home** Tab. Now you are ready to use this add-in.

### Use add-in

Note that you should select at least two rows as the first row will be considered as header.

* Prepare your Excel sheet
* Select data you'd like to convert
* Choose Mode: Flat or Nested JSON mode
* If you have subscribed "Pro Features", you can set more options
* Click on "Go" button
* You will later see the converted JSON below the "Go" button
* Later you can "copy+paste" / "copy to clipboard" JSON and save it to your computer


## Examples

**Example Excel sheet 1**


|Name|Age|Company|
|---|---|---|
|David|27|WTSolutions|
|Ton|26|WTSolutions|
|Kitty|30|Microsoft|
|Linda|30|Microsoft|
|Joe|40|Github|

> Using Flat JSON mode

**Example JSON**

```json
[
    {
        "Name": "David",
        "Age": 27,
        "Company": "WTSolutions"
    },
    {
        "Name": "Ton",
        "Age": 26,
        "Company": "WTSolutions"
    },
    {
        "Name": "Kitty",
        "Age": 30,
        "Company": "Microsoft"
    },
    {
        "Name": "Linda",
        "Age": 30,
        "Company": "Microsoft"
    },
    {
        "Name": "Joe",
        "Age": 40,
        "Company": "Github"
    }
]
```

**Example Excel sheet 2**

|id|student.name|student.familyname|student.age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|
|3|Elon|Mask|18|

> Using Flat JSON Mode

```json
[{
	"id": 1,
	"student.name": "Meimei",
	"student.familyname": "Han",
	"student.age": 12
}, {
	"id": 2,
	"student.name": "Lily",
	"student.familyname": "Jaskson",
	"student.age": 15
}, {
	"id": 3,
	"student.name": "Elon",
	"student.familyname": "Mask",
	"student.age": 18
}]
```

> Using Nested JSON mode

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
}, {
	"id": 3,
	"student": {
		"name": "Elon",
		"familyname": "Mask",
		"age": 18
	}
}]

```
