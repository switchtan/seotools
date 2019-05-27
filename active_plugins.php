<?php
include_once('./wp-load.php');


include_once ( './wp-admin/includes/plugin.php' );
$all_plugins = get_plugins();

// Save the data to the error log so you can see what the array format is like.
//print_r( $all_plugins ) ;
$needToActive= array(
    'wp-super-cache','wptouch'
);

$needToDeactive= array(
);
foreach( $all_plugins as $key => $value){
  echo '<br>'.explode('/',$key)[0].'<br>';
  $plugin_name=explode('/',$key)[0];
  if(in_array($plugin_name, $needToActive)){
    echo "exists:".$key."<br>";
    if (!is_plugin_active( $key )) {
       echo "active:".$key."<br><br>";
      activate_plugin( $key );
    }else{
      //echo "deactive:".$key."<br><br>";
      //array_push($needToDeactive,$key);
      //deactivate_plugins($needToDeactive);
    }
    
    
  }
}