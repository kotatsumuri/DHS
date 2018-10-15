<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<title>DHS</title>
<link rel="stylesheet" type="text/css" href="./stylesheets/uploadcsv.css">
</head>
<?php
// ファイル名を取得して、ユニークなファイル名に変更
$file_name = $_FILES['upfile']['name'];
$uniq_file_name = date("YmdHis") . "_" . $file_name;

// 仮にファイルがアップロードされている場所のパスを取得
$tmp_path = $_FILES['upfile']['tmp_name'];

// 保存先のパスを設定
$upload_path = '../upload/';

if (is_uploaded_file($tmp_path)) {
  // 仮のアップロード場所から保存先にファイルを移動
  if (move_uploaded_file($tmp_path, $upload_path . $uniq_file_name)) {
    // ファイルが読出可能になるようにアクセス権限を変更
    chmod($upload_path . $uniq_file_name, 0644);

    echo "<div class="."title"."><span class='filename'>". $file_name . "</span>をアップロードしました</div>";
    echo "<br><a href='map.html' class='next-btn'>結果を見る</a>";
  } else {
    echo "Error:アップロードに失敗しました。";
  }
} else {
  echo "Error:ファイルが見つかりません。";
}
$value_arry=[
  'name'=>$uniq_file_name
];
$jsonstr=json_encode($value_arry,JSON_PRETTY_PRINT);
file_put_contents("../scripts/jsons/namecsv.json",$jsonstr);

//exec('bash main.sh',$output,$status);

?>
</html>
