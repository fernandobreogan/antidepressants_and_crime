<p align="center">
  <img width="1000" height="300" src="https://github.com/breogann/Project-2.Antidepressant-prescription/Images/cover.png" alt="Datas nurturing & cleaning">
</p>


# Data enrichment & cleaning

Selection of a world-wide location for a gaming company given some criteria. Data used was a dataset with companies and FourSquare API to get locations for Starbucks. 

##  The problem ❗️ ## 
<p align="left">
  <img width="450" height="400" src="https://github.com/breogann/Project-2.Antidepressant-prescription/blob/master/Images/problem.png" alt="problem">

## The solution 🟢 ##

### Data 📊 ###

The speech accent archive _(https://accent.gmu.edu)_ has a compilation of a huge variety of speakers with different backgrounds that read the same paragraph so it can be analyzed.

In this case, only __spanish__ and __english__ speakers were used to train the model. Although speakers were not limited to a particular region, most of them belong to either the US and Spain.

### Data processing 🛠 ###
- Obtention of coordinates through MongoDB
- Formatting those coordinates
- Use the formatted data to iterate over through the API
- Place the coordinates in a map

<table border="0">
    <tr>
        <td><b style="font-size:13px">Used technologies 🔌</b></td>
        <td><b style="font-size:13px">Used libraries 📚</b></td>
    </tr>
    <tr>
        <td>
            <ul>
                <font size="1.5">
      <li>MongoDB</li>
      <li></li>
      <li></li>
      <li></li>
      </font>
            </ul>
        </td>
        <td>
            <ul>
                <font size="1.5">
      <li>Pandas</li>
      <li></li>
      <li></li>
      <li></li>
      </font>
</table>

##### To do #####
- Add more venue filters: vegan places, etc.
- Calculate minimun distance to rank possible places