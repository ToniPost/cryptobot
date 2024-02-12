<?php

// Assuming you have a database connection
$dbHost = 'localhost';
$dbUser = 'root';
$dbPassword = '';
$dbName = 'wallet_app';

$conn = new mysqli($dbHost, $dbUser, $dbPassword, $dbName);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch balance from the database
$result = $conn->query("SELECT * FROM wallet WHERE id = 1");

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $balance = $row['balance'];

    // Return balance as JSON
    echo json_encode(['balance' => $balance]);
} else {
    echo json_encode(['balance' => 0.0]);
}

$conn->close();

?>
