// Check if booking was successful
if (bookingSuccess === "True") {
    // Display pop-up message
    alert("Booking successful!");
}

if (typeof bookingSuccess !== 'undefined') {
    console.log("Booking success:", bookingSuccess); // Output the value for debugging
} else {
    console.log("bookingSuccess variable is not defined.");
}
