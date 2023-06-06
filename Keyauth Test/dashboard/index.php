<?php
error_reporting(0);

require '../keyauth.php';
require '../credentials.php';

session_start();

if (!isset($_SESSION['user_data'])) // if user not logged in
{
    header("Location: ../");
    exit();
}

$KeyAuthApp = new KeyAuth\api($name, $ownerid);

function findSubscription($name, $list)
{
    for ($i = 0; $i < count($list); $i++) {
        if ($list[$i]->subscription == $name) {
            return true;
        }
    }
    return false;
}

$username = $_SESSION["user_data"]["username"];
$subscriptions = $_SESSION["user_data"]["subscriptions"];
$subscription = $_SESSION["user_data"]["subscriptions"][0]->subscription;
$expiry = $_SESSION["user_data"]["subscriptions"][0]->expiry;

if (isset($_POST['logout'])) {
    session_destroy();
    header("Location: ../");
    exit();
}
?>
<html lang="en">

<head>
    <title>Dashboard</title>
    <script src="https://cdn.keyauth.win/dashboard/unixtolocal.js"></script>
</head>

<input type="button" value="Download" class="homebutton" id="btnHome" onClick="Javascript:window.location.href = 'https://github.com/AlexBartles/Nightmare-Remade/releases';" />

<body>
    <form method="post"><button name="logout">Logout</button></form>
    Logged in as <?php echo $username; ?>
    <br>

    <?php
    for ($i = 0; $i < count($subscriptions); $i++) {
        echo "#" . $i + 1 . " Subscription: " . $subscriptions[$i]->subscription . " - Subscription Expires: " . "<script>document.write(convertTimestamp(" . $subscriptions[$i]->expiry . "));</script>";
    }
    ?>
<body>
