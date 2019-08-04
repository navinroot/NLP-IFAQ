<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Script-Type" content="text/javascript">
<link href="ifaq.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
function validateForm()
{
	var x=document.forms["target"]["ques"].value;
	if (x==null || x=="")
	  {
	  alert("please enter your query");
	  return false;
	  }
}	
</script>
</head>

<body>
<div class="container">
<div class="head">
<img src="pic/head.png" alt="" style="width:1100px;height:150px; position:relative; top:-4px; left:-2px;">
</div>
<h1 style="align:center; color:red; position:relative; left:300px;">Welcome to iFAQ Tool</h1>
<div class="usidebar" >
	<form action="#" method="post" name="target" id="form" onsubmit="return validateForm()" enctype="multipart/form-data">
<h2 style="position:relative; top:20px; left:-10px; color:red;">Ques:</h2>
<textarea rows="2"  cols="100" name="ques" placeholder="Please place your Query here::" style="position:relative; top:-40px; left:80px;" ></textarea>
 <input  type="submit" name="submit" id="submit"  value="Submit" style="position:relative; top:-50px; left:90px;">
 <input style="color:red; position:relative; top:-50px; left:100px;"type='button' value='Reset' onClick="location.href='ifaq.php'"  name='submit1'>
</form>
</div>

<div class="dsidebar">
<?php
if((isset($_POST['submit'])) && ($_SERVER['REQUEST_METHOD'] == "POST"))
{
	$q = test_input($_POST["ques"]);
	if(strpos($q,"?") !== false)
	{
		$q=str_replace("?","",$q);
	}	
	print "<h3 style='color:red;'>Ques->".$q."?"."</h3><h5 style='color:blue;'>";
	if(strpos($q,"detail of") !== false)
	{
		$q=str_replace("detail of ","",$q);
		$c='"';
		$query=$c.$q.$c;	
	#	print $query;
		print "Ans->";
		$last_line=system("python table_info.py ".$query,$return);
	#	print $return."</h3>";
	}
	else
	{
		$c='"';
		$query=$c.$q.$c;
		print "<div style='display:none;'>";
		$last_line=system("python main2.py ".$query,$return);
	}
	print "</div>";
	#print $last_line;

	if ($last_line>0 and $last_line<11) 
	{
		$linecount=1;
		$myfile = fopen("ans/".$last_line.".txt", "r") or die("Unable to open file!");
		while(!feof($myfile))
		{
 		 	$line = fgets($myfile);
 		 	if ($line!="")
 		 	{	
 		 		print "Ans: ".$linecount."-> ".$line."<br><br>";
  				$linecount++;
  			}	
		}
		fclose($myfile);
		print "</h5>";

	}









}
function test_input($data)
{
     $data = trim($data);
     $data = stripslashes($data);
     $data = htmlspecialchars($data);
     return $data;
}



?>

</div>
<div class="lowerbar">
<h2>iFAQ</h2>
<p>
iFAQ is an intelligent answering tool that replies to the frequently asked questions by user.<br> 
This tool was developed as a 4th year Btech project under the guidence of <b><a href="http://www.tezu.ernet.in/~utpal/index.html" target="_blank">Prof. Utpal Sharma</a>, Dept. of CSE, Tezpur University.</b><br><small>Developed by Pallavi Gupta (CSB11066), Navin Kumar (CSB11076), Btech 2011-15, Dept. of CSE, Tezpur University</small></p>
</div>
</div>
</body>
</html>