# Usage

Reading [Get Started](getstarted.md) section first is strongly recommended.
 <a name="Conversiontypes"></a> 
## Conversion types
 <a name="Row"></a> 
### Row
		Note that you should select at least two rows as the first row will be considered as header.
    
If you choose 'Row' as the conversion type

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
 <a name="Nested"></a> 
### Nested

This conversion type is based on an amazing open source project [shape-json](https://github.com/ansteh/shape-json).

You need to provide a predefined schema , and Excel-to-JSON will convert your Excel sheet to JSON using provided schema.

Please read Api documentation https://github.com/ansteh/shape-json#api-documentation to prepare a schema.

**Example Excel Sheet**

<table class="table table-bordered table-striped table-condensed">
<tr>
	<th>pid</th>
	<th>contributor</th>
	<th>projectID</th>
	<th>projectName</th>
</tr>
<tr>
	<td>1</td>
	<td>jdalton</td>
	<td>1</td>
	<td>lodash</td>
</tr>
<tr>
	<td>1</td>
	<td>jdalton</td>
	<td>2</td>
	<td>docdown</td>
</tr>
<tr>
	<td>1</td>
	<td>jdalton</td>
	<td>3</td>
	<td>lodash-cli</td>
</tr>
<tr>
	<td>2</td>
	<td>contra</td>
	<td>4</td>
	<td>gulp</td>
</tr>
<tr>
	<td>3</td>
	<td>phated</td>
	<td>4</td>
	<td>gulp</td>
</tr>
</table>

**Example Schema**

```
{
  "$group[contributors](pid)": {
    "id": "pid",
    "name": "contributor",
    "$group[projects](projectID)": {
      "id": "projectID",
      "name": "projectName"
    }
  }
}
```

**Example JSON**

```
{
  "contributors": [
    {
      "id": 1,
      "name": "jdalton",
      "projects": [
        {
          "id": 1,
          "name": "lodash"
        },
        {
          "id": 2,
          "name": "docdown"
        },
        {
          "id": 3,
          "name": "lodash-cli"
        }
      ]
    },
    {
      "id": 2,
      "name": "contra",
      "projects": [
        {
          "id": 4,
          "name": "gulp"
        }
      ]
    },
    {
      "id": 3,
      "name": "phated",
      "projects": [
        {
          "id": 4,
          "name": "gulp"
        }
      ]
    }
  ]
}
```
