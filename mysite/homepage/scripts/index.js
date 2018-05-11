$(function(context) {
    return function() {
        // update the time every n seconds
        window.setInterval(function () {
            $('.browser-time').text('The current browser time is ' + new Date())
        }, 1000)

        // update server time button
        $('#server-time-button').click(function () {
            console.log(context)
            $('.server-time').load('/homepage/index.gettime')
        })
    }
}(DMP_CONTEXT.get()))