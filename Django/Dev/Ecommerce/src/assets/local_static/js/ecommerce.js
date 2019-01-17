'use strict';
$(document).ready(function () {

    /* Contact Form Handler */
    let contactForm = $(".contact-form")
    let contactFormMethod = contactForm.attr("method")
    let contactFormEndpoint = contactForm.attr("action")

    let contactFormSubmitBtn = contactForm.find("[type='submit']")
    let contactFormSubmitBtnTxt = contactFormSubmitBtn.text()

    function displaySubmitting(submitBtn, defaultText, doSubmit) {
        if (doSubmit) {
            submitBtn.addClass("disabled")
            submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
        } else {
            submitBtn.removeClass("disabled")
            submitBtn.html(defaultText)
        }

    }

    contactForm.submit(function (e) { // using instead of onClick
        e.preventDefault()

        let contactFormSubmitBtn = contactForm.find("[type='submit']")
        let contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
        let contactFormData = contactForm.serialize()
        let thisForm = $(this)
        displaySubmitting(contactFormSubmitBtn, "", true)
        console.log(contactFormData)
        $.ajax({
            method: contactFormMethod,
            url: contactFormEndpoint,
            data: contactFormData,
            success: function (data) {
                thisForm[0].reset()
                $.alert({
                    title: "Success",
                    content: data.message,
                    theme: "modern"
                })
                setTimeout(function () {
                    displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
                }, 500)

            },
            error: function (error) {
                let jsonData = error.responseJSON
                let msg = ""
                $.each(jsonData, function (key, value) { //key, value 
                    msg += key + ": " + value[0].message + "<br/>"
                })
                $.alert({
                    title: "Ooops",
                    content: msg,
                    theme: "modern"
                })
                console.log(error)
                setTimeout(function () {
                    displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })





    /* Auto Search */
    let searchForm = $(".search-form")
    let searchInput = searchForm.find("[name='q']") //input name ="q"
    let typingTimer;
    let typingInterval = 500 // 5 seconds
    let searchBtn = searchForm.find("[type='submit']")

    searchInput.keyup(function (e) {
        clearTimeout(typingTimer) // key released
        typingTimer = setTimeout(performSearch, typingInterval)
    })

    searchInput.keydown(function (e) {
        clearTimeout(typingTimer) // key down pressed
    })

    function displaySearching() {
        searchBtn.addClass("disabled")
        searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
    }

    function performSearch() {
        displaySearching()
        searchBtn.html()
        let query = searchInput.val()
        setTimeout(function () {
            window.location.href = `/search/?q=${query}`
        }, 1000)
    }




    /* Cart + Add Products */
    $(document).on("submit", ".form-product-ajax", function (e) {
        e.preventDefault();
        //console.log("Form is not sending")
        let thisForm = $(this) // the form itself
        let actionURL = thisForm.attr('action')
        let actionEndPoint = thisForm.attr('data-endpoint')
        let httpMethod = thisForm.attr('method')
        let formData = thisForm.serialize()
        $.ajax({
            url: actionEndPoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                let submitSpan = thisForm.find(".submit-span")
                if (data.added) {
                    submitSpan.html("In cart<button type='submit' class='btn btn-info'>Remove</button>")
                } else {
                    submitSpan.html("<button type='submit' class='btn btn-success'>Add to cart</button>")
                }
                let navbarCount = $(".navbar-cart-count")
                navbarCount.text(data.cartItemCount) // updates cart icon
                let currentPath = window.location.href
                console.log(currentPath)
                if (currentPath.indexOf("update") != 1) { // if carts is in current path
                    refreshCart()
                }
            },
            error: function (errorData) {
                $.alert({
                    title: "Ooops",
                    content: "An error ocurred",
                    theme: "modern"
                })
                console.log(errorData)
            }

        })
    })

    function refreshCart() {
        console.log('In current Cart')
        let cartTable = $(".cart-table")
        let cartBody = cartTable.find(".cart-body")
        let productRows = cartBody.find(".cart-product")
        let currentUrl = window.location.href

        let refreshCartUrl = '/api/cart/update/cart'
        let refreshCartMethod = "GET"
        let data = {}

        $.ajax({
            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            success: function (data) {
                let hiddenCartItemRemoveForm = $(".cart-item-remove-form")

                if (data.products.length > 0) {
                    productRows.html(" ")
                    let i = data.products.length
                    $.each(data.products, function (index, value) {
                        console.log(`Value is ${value.id}`)
                        let newCartItemRemove = hiddenCartItemRemoveForm.clone()
                        newCartItemRemove.css('display', 'block')
                        newCartItemRemove.find(".cart-item-product-id").val(value.id)
                        cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + " </td><tr>")
                        i--
                    })


                    cartBody.find(".cart-subtotal").text(data.subtotal)
                    cartBody.find(".cart-total").text(data.total)
                } else {
                    window.location.href = currentUrl
                }

            },
            error: function (errorData) {
                $.alert({
                    title: "Ooops",
                    content: "An error ocurred",
                    theme: "modern"
                })
                console.log(errorData)
            }
        })
    }
})