import re

s = '<!--[if gte mso 9]><xml>  <w:WordDocument>   <w:View>Normal</w:View>   <w:Zoom>0</w:Zoom>   <w:TrackMoves/>   <w:TrackFormatting/>   <w:HyphenationZone>21</w:HyphenationZone>   <w:PunctuationKerning/>   <w:ValidateAgainstSchemas/>   <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>   <w:IgnoreMixedContent>false</w:IgnoreMixedContent>   <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>   <w:DoNotPromoteQF/>   <w:LidThemeOther>DE</w:LidThemeOther>   <w:LidThemeAsian>X-NONE</w:LidThemeAsian>   <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>   <w:Compatibility>    <w:BreakWrappedTables/>    <w:SnapToGridInCell/>    <w:WrapTextWithPunct/>    <w:UseAsianBreakRules/>    <w:DontGrowAutofit/>    <w:SplitPgBreakAndParaMark/>    <w:EnableOpenTypeKerning/>    <w:DontFlipMirrorIndents/>    <w:OverrideTableStyleHps/>    <w:UseFELayout/>   </w:Compatibility>   <w:DoNotOptimizeForBrowser/>   <m:mathPr>    <m:mathFont m:val=&quot;Cambria Math&quot;/>    <m:brkBin m:val=&quot;before&quot;/>    <m:brkBinSub m:val=&quot;&#45;-&quot;/>    <m:smallFrac m:val=&quot;off&quot;/>    <m:dispDef/>    <m:lMargin m:val=&quot;0&quot;/>    <m:rMargin m:val=&quot;0&quot;/>    <m:defJc m:val=&quot;centerGroup&quot;/>    <m:wrapIndent m:val=&quot;1440&quot;/>    <m:intLim m:val=&quot;subSup&quot;/>    <m:naryLim m:val=&quot;undOvr&quot;/>   </m:mathPr></w:WordDocument> </xml><![endif]-->LALA'

r = re.sub(r"<!--.*-->", "", s)

print(r)