# Usage
		Reading [Get Started](getstarted.md) section first is strongly recommended.
	
## Conversion types
### Row
		Note that you should have at least two rows as the first row will be considered as header.
		Note that all data in active sheet will be collected for json conversion.

If you choose 'Row' as the conversion type

* This add-in will first collect all the data in the active sheet.
* The first row will be interpreted as header.
* The following rows will be mapped with header as you can see in the following example.

**Example Excel sheet**

<table class="table table-bordered table-striped table-condensed">
<th>
	<td>Name</td>
	<td>Age</td>
	<td>Company</td>
</th>
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
{}
```

### Nested

This conversion type is based on an amazing open source project [shape-json](https://github.com/ansteh/shape-json).

You need to provide a predefined schema , and Excel-to-JSON will convert your Excel sheet to JSON using provided schema.

Please read Api documentation https://github.com/ansteh/shape-json#api-documentation to prepare a schema.

**Example Excel Sheet**

<table class="table table-bordered table-striped table-condensed">
<th>
	<td>pid</td>
	<td>contributor</td>
	<td>projectID</td>
	<td>projectName</td>
</th>
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

