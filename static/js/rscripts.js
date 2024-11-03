document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signupForm');

    signupForm.addEventListener('submit', function(event) {
        if (!isValidUsername(signupForm.username.value)) {
            showError(signupForm.username, 'Please enter a valid username.');
            event.preventDefault();
            return;
        }

        if (!isValidEmail(signupForm.email.value)) {
            showError(signupForm.email, 'Please enter a valid email address.');
            event.preventDefault();
            return;
        }

        if (!isValidMobileNumber(signupForm.mobile_number.value)) {
            showError(signupForm.mobile_number, 'Please enter a valid mobile number (starting with 9, 8, 7, or 6 and containing 10 digits).');
            event.preventDefault();
            return;
        }

        if (!isValidPincode(signupForm.pincode.value)) {
            showError(signupForm.pincode, 'Please enter a valid 6-digit pincode.');
            event.preventDefault();
            return;
        }

        if (!isValidAddress(signupForm.address.value)) {
            showError(signupForm.address, 'Please enter a valid address.');
            event.preventDefault();
            return;
        }

        if (!isValidPassword(signupForm.password.value)) {
            showError(signupForm.password, 'Password must be at least 8 characters long.');
            event.preventDefault();
            return;
        }
    });

    function isValidUsername(username) {
        return username.trim().length > 0;
    }

    function isValidEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const domainRegex = /^[^\s@]+@[^\s@]+\.[com]{3}$/;
        return regex.test(email) && domainRegex.test(email);
    }

    function isValidMobileNumber(mobileNumber) {
        return /^[7896]\d{9}$/.test(mobileNumber);
    }

    function isValidPincode(pincode) {
        return /^\d{6}$/.test(pincode);
    }

    function isValidAddress(address) {
        return address.trim().length > 0;
    }

    function isValidPassword(password) {
        return password.length >= 8;
    }

    function showError(input, message) {
        const formGroup = input.parentElement;
        const errorMessage = formGroup.querySelector('.error-message');
        errorMessage.textContent = message;
    }
});
