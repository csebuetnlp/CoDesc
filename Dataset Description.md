# Details of CoDesc
  
## Files description
[CoDesc](https://drive.google.com/file/d/14t7fYsW0a09mfBmFJhjsZv-3obnLnNmS) contains the following files that consists the 4.2m CoDesc dataset and related information.  

1. CoDesc.json:  
    * List of python dictionaries type  
    * Each entry has the following keys:  
        - id: unique id in CoDesc dataset  
        - src: source dataset  
        - src_div: which subset the entry was taken from, e.g. train, test, etc.  
        - src_idx: idx in source subset  
        - code: java function  
        - nl: natural language description after initial filtering  
        - original_code: source code taken from source  
        - original_nl: natural language description taken from source  
        - partition: "train", "valid" or "test"  
  
2. src2id.json:  
	* Dictionary type  
	* src2id[src][src_div] is a list of ids from CoDesc dataset  
	* src -> src_div:   
		- "CodeSearchNet-Java" -> "test", "valid", "train", "removed"  
		- "FunCom" -> "none"   
		- "DeepCom" -> "test", "valid", "train"  
		- "CONCODE" -> "test", "valid", "train"   
		- "CodeSearchNet-Py2Java" -> "full", "truncated"  
  
3. id2src.csv:  
	* csv type  
	* Columns:   
		- id: unique id in CoDesc dataset  
		- src: source dataset  
		- src_div: which subset the entry was taken from, e.g. train, test, etc.  
		- src_idx: idx in source subset   
  
4. src_len.csv  
	* csv type  
	* Columns:  
		- src: source dataset  
		- src_div: which subset the entry was taken from, e.g. train, test, etc.  
		- len: number of datapoints under this subset  
  
5. partition2id.json  
	* Dictionary type  
	* partition2id["train"], partition2id["valid"], and partition2id["test"] are list of ids in CoDesc dataset corresponding to the partition they belong to.  


## Dataset Statistics
<!-- <style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-9anz{border-color:#333333;text-align:right;vertical-align:top}
.tg .tg-lqy6{text-align:right;vertical-align:top}
.tg .tg-nehb{border-color:#333333;font-family:Arial, Helvetica, sans-serif !important;;text-align:center;vertical-align:top}
.tg .tg-ao2g{border-color:#333333;text-align:center;vertical-align:top}
.tg .tg-de2y{border-color:#333333;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-dvpl{border-color:inherit;text-align:right;vertical-align:top}
</style> -->
<table class="tg">
<thead>
  <tr>
    <th class="tg-nehb" rowspan="2"><span style="font-weight:400;font-style:normal"><b>Name</b></span></th>
    <th class="tg-nehb" rowspan="2"><b>#Projects</b></th>
    <th class="tg-nehb" rowspan="2"><span style="font-weight:400;font-style:normal"><b>#Raw </span><br>data</b></th>
    <th class="tg-ao2g" rowspan="2"><b>#Clean <br>data</b></th>
    <th class="tg-ao2g" colspan="3"><b>Code</b></th>
    <th class="tg-ao2g" colspan="3"><b>NL</b></th>
  </tr>
  <tr>
    <td class="tg-ao2g"><b>#Unique<br>tokens</b></td>
    <td class="tg-ao2g"><b>Avg <br>len</b></td>
    <td class="tg-ao2g"><span style="font-style:normal"><b>≤ 200 (%)</b></span></td>
    <td class="tg-ao2g"><b>#Unique<br>tokens</b></td>
    <td class="tg-ao2g"><b>Avg <br>len</b></td>
    <td class="tg-ao2g"><span style="font-weight:400;font-style:normal"><b>≤ 50 (%)</b></span></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-de2y">CSN-Java</td>
    <td class="tg-9anz">N/A</td>
    <td class="tg-9anz">542,991</td>
    <td class="tg-9anz">490,169</td>
    <td class="tg-9anz">284,214</td>
    <td class="tg-9anz">140.41</td>
    <td class="tg-9anz">83.42</td>
    <td class="tg-9anz">168,507</td>
    <td class="tg-9anz">25.14</td>
    <td class="tg-9anz">89.42</td>
  </tr>
  <tr>
    <td class="tg-de2y">DeepCom</td>
    <td class="tg-9anz">9,714</td>
    <td class="tg-9anz">588,108</td>
    <td class="tg-9anz">424,028</td>
    <td class="tg-9anz">306,422</td>
    <td class="tg-9anz">128.35</td>
    <td class="tg-9anz">84.04</td>
    <td class="tg-9anz">91,933</td>
    <td class="tg-9anz">17.80</td>
    <td class="tg-9anz">94.76</td>
  </tr>
  <tr>
    <td class="tg-de2y">FunCom</td>
    <td class="tg-9anz">28,000</td>
    <td class="tg-9anz">2,149,121</td>
    <td class="tg-9anz">2,130,247</td>
    <td class="tg-9anz">469,354</td>
    <td class="tg-9anz">51.30</td>
    <td class="tg-9anz">99.83</td>
    <td class="tg-9anz">399,338</td>
    <td class="tg-9anz">15.52</td>
    <td class="tg-9anz">95.87</td>
  </tr>
  <tr>
    <td class="tg-de2y">CONCODE</td>
    <td class="tg-9anz">33,000</td>
    <td class="tg-9anz">2,184,310</td>
    <td class="tg-9anz">733,040</td>
    <td class="tg-9anz">131,852</td>
    <td class="tg-9anz">33.75</td>
    <td class="tg-9anz">99.99</td>
    <td class="tg-9anz">166,239</td>
    <td class="tg-9anz">14.87</td>
    <td class="tg-9anz">96.27</td>
  </tr>
  <tr>
    <td class="tg-de2y">CSN-Py2Java</td>
    <td class="tg-9anz">N/A</td>
    <td class="tg-9anz">456,000</td>
    <td class="tg-9anz">434,032</td>
    <td class="tg-9anz">414,018</td>
    <td class="tg-9anz">163.78</td>
    <td class="tg-9anz">72.32</td>
    <td class="tg-9anz">223,277</td>
    <td class="tg-9anz">57.11</td>
    <td class="tg-9anz">68.69</td>
  </tr>
  <tr>
    <td class="tg-de2y">CoDesc (All)</td>
    <td class="tg-9anz">N/A</td>
    <td class="tg-9anz">5,920,530</td>
    <td class="tg-9anz">4,211,516</td>
    <td class="tg-9anz">1,128,909</td>
    <td class="tg-9anz">77.97</td>
    <td class="tg-9anz">93.53</td>
    <td class="tg-9anz">813,078</td>
    <td class="tg-9anz">21.04</td>
    <td class="tg-9anz">92.28</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="10">Balanced <span style="font-style:italic"><i>train-valid-test</i></span> split for CoDesc data</td>
  </tr>
  <tr>
    <td class="tg-0lax">train</td>
    <td class="tg-lqy6">-</td>
    <td class="tg-lqy6">-</td>
    <td class="tg-lqy6">3,369,218</td>
    <td class="tg-lqy6">991,395</td>
    <td class="tg-lqy6">78.01</td>
    <td class="tg-lqy6">93.53</td>
    <td class="tg-lqy6">718,204</td>
    <td class="tg-lqy6">21.05</td>
    <td class="tg-lqy6">92.28</td>
  </tr>
  <tr>
    <td class="tg-0lax">valid</td>
    <td class="tg-lqy6">-</td>
    <td class="tg-lqy6">-</td>
    <td class="tg-lqy6">421,149</td>
    <td class="tg-lqy6">269,435</td>
    <td class="tg-lqy6">77.73</td>
    <td class="tg-lqy6">93.51</td>
    <td class="tg-lqy6">188,145</td>
    <td class="tg-lqy6">21.08</td>
    <td class="tg-lqy6">92.26</td>
  </tr>
  <tr>
    <td class="tg-0pky">test</td>
    <td class="tg-dvpl">-</td>
    <td class="tg-dvpl">-</td>
    <td class="tg-dvpl">421,149</td>
    <td class="tg-dvpl">269,318</td>
    <td class="tg-dvpl">77.88</td>
    <td class="tg-dvpl">93.55</td>
    <td class="tg-dvpl">187,230</td>
    <td class="tg-dvpl">20.97</td>
    <td class="tg-dvpl">92.33</td>
  </tr>
</tbody>
</table>

