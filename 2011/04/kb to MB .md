<span style="color:red; font-weight: blod;">本文参考了 <http://otnv.pixnet.net/blog/post/29073136> </span>


代码：     
<pre class="prettyprint">
function readablizeBytes(bytes) {
    var s = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB'];
    var e = Math.floor(Math.log(bytes)/Math.log(1024));
    return (bytes/Math.pow(1024, Math.floor(e))).toFixed(2)+" "+s[e];
}
</pre>


用法：    
<pre class="prettyprint">
readablizeBytes(8589312); // return 8.19 MB
</pre>


实例：     
Firefox 扩展 [DiB](https://addons.mozilla.org/zh-CN/firefox/addon/dib/) 的功能如下：     
![DiB1][]       
可以看出此扩展是以 Bytes 为单位的，不够友好。现在用本文的代码对源代码进行改动，达到文件大小智能显示的效果：     
![DiB2][]       
只须改动文件 扩展\chrome\content\overlay.js 即可      
改动前：        
<pre class="prettyprint">
var showDialogAddonDiB =
{
  init: function()
  {
    if ("contentLength" in dialog.mLauncher)
    {
      var bytes = dialog.mLauncher.contentLength;
      var type = dialog.dialogElement("type");
      if (bytes != -1)
      {
        type.value += " (" + bytes.toLocaleString() + " Bytes)";
        type.setAttribute("tooltiptext", type.value);
      }
    }
  }
};
dialog.mDialog.addEventListener("load", function() { showDialogAddonDiB.init(); }, false);

</pre>      
改动后：        
<pre class="prettyprint">
var showDialogAddonDiB =
{
  init: function()
  {
    if ("contentLength" in dialog.mLauncher)
    {
      var bytes = dialog.mLauncher.contentLength;
      var type = dialog.dialogElement("type");
      if (bytes != -1)
      {
        type.value += " ( " + readablizeBytes(bytes).toLocaleString() + " )";
        type.setAttribute("tooltiptext", type.value);
      }
    }
    
    function readablizeBytes(bytes) {
        var s = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB'];
        var e = Math.floor(Math.log(bytes)/Math.log(1024));
        return (bytes/Math.pow(1024, Math.floor(e))).toFixed(2)+" "+s[e];
    }
  }
  
};
dialog.mDialog.addEventListener("load", function() { showDialogAddonDiB.init(); }, false);

</pre>


  [DiB1]:  http://mzgphotos.appspot.com/showimage/158007/
  [DiB2]:  http://mzgphotos.appspot.com/showimage/155014/

