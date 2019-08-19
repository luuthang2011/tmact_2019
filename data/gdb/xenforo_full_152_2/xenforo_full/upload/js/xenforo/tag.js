/*
 * XenForo tag.min.js
 * Copyright 2010-2015 XenForo Ltd.
 * Released under the XenForo License Agreement: http://xenforo.com/license-agreement
 */
(function(b){XenForo.TagInput=function(b){this.__construct(b)};XenForo.TagInput.prototype={__construct:function(g){var f=g.uniqueId().attr("id"),a=g.data("extra-class");g.tagsInput({width:"",minInputWidth:"100%",maxInputWidth:"100%",height:"",defaultText:"",wrapperExtraClass:"textCtrl"+(a?" "+a:""),removeWithBackspace:!0,autosize:!1,unique:!0});var c=b("#"+f+"_tag");c.addClass("AcSingle").data("acurl","index.php?misc/tag-auto-complete");XenForo.create("XenForo.AutoComplete",c);c.on("AutoComplete",
function(b,a){c.val("");g.addTag(a.inserted,{unique:!0})});c.on("paste",function(){setTimeout(function(){var e=c.val().split(",");if(e.length>1){for(var a=0;a<e.length;a++)e[a]=b.trim(e[a]),e[a].length&&g.addTag(e[a],{unique:!0});c.val("")}},0)});c.closest("form").on("submit AutoValidationBeforeSubmit",function(){var b=c.val();b.length&&(g.addTag(b,{unique:!0}),c.val(""))});c.on("focus",function(){c.closest(".textCtrl").addClass("Focus")});c.on("blur",function(){c.closest(".textCtrl").removeClass("Focus")});
g.prop("autofocus")&&(g.prop("autofocus",!1),c.prop("autofocus",!0),c.focus())}};XenForo.TagEditorForm=function(b){this.__construct(b)};XenForo.TagEditorForm.prototype={__construct:function(g){var f=function(b){b.ajaxData.redirect&&XenForo.redirect(b.ajaxData.redirect)};g.on("AutoValidationComplete",function(a){a.preventDefault();if(!a.ajaxData.templateHtml||!a.ajaxData.isTagList)f(a);else{var c=g.closest(".xenOverlay");if(!c.length||!c.data("overlay"))f(a);else{var c=c.data("overlay"),e=c.getTrigger().closest(".TagContainer");
e.length?(a.preventDefault(),a=b(b.parseHTML(a.ajaxData.templateHtml)),e.replaceWith(a),a.parent().xfActivate(),c.close()):f(a)}}})}};XenForo.register("input.TagInput","XenForo.TagInput");XenForo.register("form.TagEditorForm","XenForo.TagEditorForm")})(jQuery,this,document);
(function(b){var g=[],f=[];b.fn.doAutosize=function(a){var c=b(this).data("minwidth"),e=b(this).data("maxwidth"),d="",f=b(this),j=b("#"+b(this).data("tester_id"));if(d!==(d=f.val()))d=d.replace(/&/g,"&amp;").replace(/\s/g," ").replace(/</g,"&lt;").replace(/>/g,"&gt;"),j.html(d),j=j.width(),a=j+a.comfortZone>=c?j+a.comfortZone:c,j=f.width(),(a<j&&a>=c||a>c&&a<e)&&f.width(a)};b.fn.resetAutosize=function(a){var c=b(this).data("minwidth")||a.minInputWidth||b(this).width(),a=b(this).data("maxwidth")||
a.maxInputWidth||b(this).closest(".taggingInput").width()-a.inputPadding,e=b(this),d=b("<tester/>").css({position:"absolute",top:-9999,left:-9999,width:"auto",fontSize:e.css("fontSize"),fontFamily:e.css("fontFamily"),fontWeight:e.css("fontWeight"),letterSpacing:e.css("letterSpacing"),whiteSpace:"nowrap"}),f=b(this).attr("id")+"_autosize_tester";!b("#"+f).length>0&&(d.attr("id",f),d.appendTo("body"));e.data("minwidth",c);e.data("maxwidth",a);e.data("tester_id",f);e.css("width",c)};b.fn.addTag=function(a,
c){c=jQuery.extend({focus:!1,callback:!0},c);this.each(function(){var e=b(this).attr("id"),d=b(this).val().split(g[e]);d[0]==""&&(d=[]);a=jQuery.trim(a);if(c.unique){var h=b(this).tagExist(a);h==!0&&b("#"+e+"_tag").addClass("not_valid")}else h=!1;if(a!=""&&h!=!0){b("<span>").addClass("tag").append(b("<span>").text(a).append("&nbsp;&nbsp;"),b("<a>",{href:"#",title:"",text:"x"}).click(function(){return b("#"+e).removeTag(escape(a))})).insertBefore("#"+e+"_addTag");d.push(a);b("#"+e+"_tag").val("");
c.focus?b("#"+e+"_tag").focus():b("#"+e+"_tag").blur();b.fn.tagsInput.updateTagsField(this,d);if(c.callback&&f[e]&&f[e].onAddTag)h=f[e].onAddTag,h.call(this,a);if(f[e]&&f[e].onChange){var j=d.length,h=f[e].onChange;h.call(this,b(this),d[j-1])}}});return!1};b.fn.removeTag=function(a){a=unescape(a);this.each(function(){var c=b(this).attr("id"),e=b(this).val().split(g[c]);b("#"+c+"_tagsinput .tag").remove();str="";for(i=0;i<e.length;i++)e[i]!=a&&(str=str+g[c]+e[i]);b.fn.tagsInput.importTags(this,str);
f[c]&&f[c].onRemoveTag&&f[c].onRemoveTag.call(this,a)});return!1};b.fn.tagExist=function(a){var c=b(this).attr("id"),c=b(this).val().split(g[c]);return jQuery.inArray(a,c)>=0};b.fn.importTags=function(a){id=b(this).attr("id");b("#"+id+"_tagsinput .tag").remove();b.fn.tagsInput.importTags(this,a)};b.fn.tagsInput=function(a){var c=jQuery.extend({interactive:!0,defaultText:"add a tag",minChars:0,width:"300px",height:"100px",autocomplete:{selectFirst:!1},wrapperExtraClass:"",hide:!0,delimiter:",",unique:!0,
removeWithBackspace:!0,autosize:!0,comfortZone:20,inputPadding:12},a);this.each(function(){c.hide&&b(this).hide();var a=b(this).attr("id");if(!a||g[b(this).attr("id")])a=b(this).attr("id","tags"+(new Date).getTime()).attr("id");var d=jQuery.extend({pid:a,real_input:"#"+a,holder:"#"+a+"_tagsinput",input_wrapper:"#"+a+"_addTag",fake_input:"#"+a+"_tag"},c);g[a]=d.delimiter;if(c.onAddTag||c.onRemoveTag||c.onChange)f[a]=[],f[a].onAddTag=c.onAddTag,f[a].onRemoveTag=c.onRemoveTag,f[a].onChange=c.onChange;
var h='<div id="'+a+'_tagsinput" class="taggingInput '+c.wrapperExtraClass+'"><div id="'+a+'_addTag" class="addTag">';c.interactive&&(h=h+'<input id="'+a+'_tag" value="" data-default="'+c.defaultText+'" />');h+='</div><div class="tagsClear"></div></div>';b(h).insertAfter(this);b(d.holder).css("width",c.width);b(d.holder).css("min-height",c.height);b(d.holder).css("height","100%");b(d.real_input).val()!=""&&b.fn.tagsInput.importTags(b(d.real_input),b(d.real_input).val());if(c.interactive){b(d.fake_input).val(b(d.fake_input).attr("data-default"));
b(d.fake_input).resetAutosize(c);b(d.holder).bind("click",d,function(a){b(a.data.fake_input).focus()});b(d.fake_input).bind("focus",d,function(a){b(a.data.fake_input).val()==b(a.data.fake_input).attr("data-default")&&b(a.data.fake_input).val("")});if(c.autocomplete_url!=void 0){autocomplete_options={source:c.autocomplete_url};for(attrname in c.autocomplete)autocomplete_options[attrname]=c.autocomplete[attrname];jQuery.Autocompleter!==void 0?(b(d.fake_input).autocomplete(c.autocomplete_url,c.autocomplete),
b(d.fake_input).bind("result",d,function(d,f){f&&b("#"+a).addTag(f[0]+"",{focus:!0,unique:c.unique})})):jQuery.ui.autocomplete!==void 0&&(b(d.fake_input).autocomplete(autocomplete_options),b(d.fake_input).bind("autocompleteselect",d,function(a,d){b(a.data.real_input).addTag(d.item.value,{focus:!0,unique:c.unique});return!1}))}b(d.fake_input).bind("keypress",d,function(a){var d=a.which==a.data.delimiter.charCodeAt(0);if(d||a.which==13){if(a.which==13&&b(a.data.fake_input).val().length==0)return!0;
a.preventDefault();var e=b(a.data.fake_input),f=e[0],g=e.val(),h=g.length,l=!1,k=null;try{if("selectionStart"in f)l=f.selectionStart<h,k=f.selectionStart;else if(document.selection){f.focus();var m=document.selection.createRange(),n=m.text.length;m.moveStart("character",-h);k=m.text.length-n;l=k<h}}catch(o){}l&&d?(d=g.substr(0,k),g=g.substr(k),b(a.data.real_input).addTag(d,{focus:!0,unique:c.unique}),e.val(b.trim(g)),f.setSelectionRange&&f.setSelectionRange(0,0)):a.data.minChars<=h&&(!a.data.maxChars||
a.data.maxChars>=h)&&b(a.data.real_input).addTag(g,{focus:!0,unique:c.unique});e.resetAutosize(c);return!1}else a.data.autosize&&b(a.data.fake_input).doAutosize(c)});d.removeWithBackspace&&b(d.fake_input).bind("keydown",function(a){if(a.keyCode==8&&b(this).val()==""){a.preventDefault();var a=b(this).closest(".taggingInput").find(".tag:last").text(),c=b(this).attr("id").replace(/_tag$/,""),a=a.replace(/[\s]+x$/,"");b("#"+c).removeTag(escape(a));b(this).trigger("focus")}});b(d.fake_input).blur();d.unique&&
b(d.fake_input).keydown(function(a){(a.keyCode==8||String.fromCharCode(a.which).match(/\w+|[\u00e1\u00e9\u00ed\u00f3\u00fa\u00c1\u00c9\u00cd\u00d3\u00da\u00f1\u00d1,/]+/))&&b(this).removeClass("notValid")})}});return this};b.fn.tagsInput.updateTagsField=function(a,c){var e=b(a).attr("id");b(a).val(c.join(g[e]))};b.fn.tagsInput.importTags=function(a,c){b(a).val("");var e=b(a).attr("id"),d=c.split(g[e]);for(i=0;i<d.length;i++)b(a).addTag(d[i],{focus:!1,callback:!1});f[e]&&f[e].onChange&&f[e].onChange.call(a,
a,d[i])}})(jQuery);
