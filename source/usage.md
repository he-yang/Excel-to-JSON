# Usage

This documentation is written for Excel-to-JSON version 2.1.0

Reading [Get Started](getstarted.md) section first is strongly recommended.

    Line break in an Excel cell will be rendered as `\n`

 <a name="Conversiontypes"></a> 
## Conversion

		Note that you should select at least two rows as the first row will be considered as header.
  

* This add-in will first collect all selected data in the active sheet.
* The first row will be interpreted as header.
* The following rows will be mapped with header as you can see in the following example.

## Conversion Mode
* Flat JSON mode
    * Simply convert Excel datasheet to a flat JSON.
* Nested JSON mode
    * First convert Excel datasheet to a flat JSON
    * then, unflatten an object with delimited keys using "Flat" [https://www.npmjs.com/package/flat](https://www.npmjs.com/package/flat)
    * unflatten() is called by Excel-to-JSON, with delimiter as ".", overwrite as true. If you have subscribed "Pro Features", you can set other delimeters.

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

## Video Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hvj-O5aIzD0?si=yQdYvZkeKM6hMj6S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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


<a name="jsonOutput"></a>
### JSON Output

There are several ways for you to save the generated JSON to your local computer.

* Copy and Paste. Once JSON generated, you will see them in the add-in, and you can simply copy and paste them anywhere you want.
* Copy to Clipboard.(Not applicable to Mac users) Once JSON generated, you can find the "Copy to Clipboard" button, click on the button, and you will have JSON on your clipboard.

## Pro Features
Excel-to-JSON offers Pro Features for users with a valid subscription:

* **Nested Delimiter**: Supports custom delimiters (/, _, .) for nested JSON keys
* **Empty Cell Handling**: Three options for empty cells: empty string "", JSON null, or exclude
* **Boolean Format**: Three boolean conversion formats: JSON true/false, string "true"/"false", or number 1/0
* **Date Format**: Date conversion options: days since 1990-01-01 or ISO 8601 string format

Details of Pro Features can be found in [Pro Features](profeatures.md) section.
