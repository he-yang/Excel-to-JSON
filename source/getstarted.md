# 1. Get Started
 <a name="Introduction"></a> 
[中文](https://excel-to-json.wtsolutions.cn/zh-cn/latest/getstarted.html)

Excel to JSON by WTSolutions is a **Microsoft Excel add-in** or **Web Application** which can convert Excel to JSON, both Flat and Nested JSON can be converted.


# 2. Requirements
 <a name="Requirements"></a>
`Option 1. Load Excel to JSON in Web Browser`
* A web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.

`Option 2. Side-load Excel to JSON in Excel` (recommended)
* Excel 2013 Service Pack 1 or later, 
* Excel 2016 for Mac, 
* Excel 2016 or later, 
* Excel Online, 
* Office 365 etc.


# 3. Quick Start
<a name="Quickstarted"></a> 
This quick start is for v 3.1.0


## 3.1 (Side-)Load Excel to JSON

`Option 1. Load Excel to JSON in Web Browser`
* Open a web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.
* Open the following URL in your web browser: <a href="https://s.wtsolutions.cn/excel-to-json.html" target="_blank">https://s.wtsolutions.cn/excel-to-json.html</a>


`Option 2. Side-load Excel to JSON in Excel` (recommended)
* Open a new datasheet in Excel 2013/2016 or Excel Online or Office 365.
* **Home** Tab or **Insert** Tab > Add-ins
* In the search box, type in "Excel to JSON"
* Follow the instructions on the screen to install the add-in, and you will see an button JSON-to-Excel added to your **Home** Tab.
* **Home** Tab > Excel to JSON > Convert
* Now you are ready to use this add-in.

### Video Guide to Get add-in (side-load in Excel)

<iframe width="560" height="315" src="https://www.youtube.com/embed/tN6lFjjhRfM?si=Yeypz-TplPjX1sWp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

 <a name="Useadd-in"></a> 

## 3.2 Use Excel to JSON

* Prepare your Excel sheet
* Load your Excel Data in one of the two ways:
    1. `Load Excel to JSON in web browser`: Copy and Paste your Excel data in the text area, or
    2. `Side-load Excel to JSON in Excel`: Select your date directly from Excel worksheet or let Excel to JSON to convert all (visible) sheets from Excel.
* Set Conversion Settings
* Click on "Go" button
* You will later see the converted JSON below the "Go" button

### Input Excel Data

There are two ways for you to input Excel data to Excel-to-JSON:

* `Load Excel to JSON in web browser`
    *  Copy and Paste your Excel data in the text area
    *  You can copy and paste your Excel data from Excel, Google Sheets, or any other Excel-compatible software, data are seperated by Tab
    *  You can also copy and paste comma seperated CSV data
* `Side-load Excel to JSON in Excel`: 
    * Select your data directly from Excel worksheet using your mouse.
    * Or, let Excel to JSON to convert all visible sheets from Excel. [Pro Feature]
    * Or, let Excel to JSON to convert all sheets from Excel. [Pro Feature]


### Output JSON export

There are several ways for you to save the generated JSON to your local computer.

* `Copy and Paste`. Once JSON generated, you will see them in a textarea, and you can simply copy and paste them anywhere you want.
* `Copy to Clipboard`. Once JSON generated, you can find the "Copy to Clipboard" button, click on the button, and you will have JSON on your clipboard.
* `Save to File`.(Not available to `Excel for Mac` users) Once JSON generated, you can find the "Save As" button, click on the button, and you will be prompted to save the JSON to a file.

### Video Guide to Use add-in

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hvj-O5aIzD0?si=yQdYvZkeKM6hMj6S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 3.3 Conversion Settings

    Line break in an Excel cell will be rendered as `\n`


### Select Header, Row/Column
By default, Excel to JSON took the first row as header, but optionally, you can select "First Column as Header".

If `First Row as Header` selected:

The first (left) column will be considered as the header column(keys for JSON object), and columns on the right will become values for JSON object."

If `First Column as Header` selected:

The first (top) row will be considered as the header row(keys for JSON object), and row below will become values for JSON object.


### Conversion Mode
* `Flat JSON mode`
    * Simply convert Excel datasheet to a flat JSON.
* `Nested JSON mode`
    * First convert Excel datasheet to a flat JSON
    * then, unflatten an object with delimited keys using "Flat" [https://www.npmjs.com/package/flat](https://www.npmjs.com/package/flat)
    * unflatten() is called by Excel-to-JSON, with delimiter as ".", overwrite as true. If you have subscribed "Pro Features", you can set other delimeters.

### Nested JSON Key Delimiter

The delimiter used to separate nested properties in the JSON output.

- `Dot (.)`
- `Underscore (_)` [Pro Feature]
- `Double Underscore (__)` [Pro Feature]
- `Slash (/)` [Pro Feature]

### Other Settings

Other settings will be described in [Pro Features](profeatures.md)

# 4. Examples


## 4.1 Example Excel sheet 1


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

## 4.2 Example Excel sheet 2

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

> Using Nested JSON mode, and dot . as delimiter

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

