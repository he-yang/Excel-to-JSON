# Usage

This documentation is written for Excel-to-JSON version 1.4.0.0

Reading [Get Started](getstarted.md) section first is strongly recommended.

    Line break in an Excel cell will be rendered as <br>
 <a name="Conversiontypes"></a> 
## Conversion

		Note that you should select at least two rows as the first row will be considered as header.
  

* This add-in will first collect all selected data in the active sheet.
* The first row will be interpreted as header.
* The following rows will be mapped with header as you can see in the following example.

**Example Excel sheet**

<table class="table table-bordered table-striped table-condensed">
<tr>
	<th>Name</th>
	<th>Age</th>
	<th>Company</th>
</tr>
<tr>
	<td>David</td>
	<td>27</td>
	<td>WTSolutions</td>
</tr>
<tr>
	<td>Ton</td>
	<td>26</td>
	<td>WTSolutions</td>
</tr>
<tr>
	<td>Kitty</td>
	<td>30</td>
	<td>Microsoft</td>
</tr>
<tr>
	<td>Linda</td>
	<td>30</td>
	<td>Microsoft</td>
</tr>
<tr>
	<td>Joe</td>
	<td>40</td>
	<td>Github</td>
</tr>
</table>

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



<a name="jsonOutput"></a>
### JSON Output

There are several ways for you to save the generated JSON to your local computer.

* Copy and Paste. Once JSON generated, you will see them in the add-in, and you can simply copy and paste them anywhere you want.
* Copy to Clipboard.(Not applicable to Mac users) Once JSON generated, you can find the "Copy to Clipboard" button, click on the button, and you will have JSON on your clipboard.