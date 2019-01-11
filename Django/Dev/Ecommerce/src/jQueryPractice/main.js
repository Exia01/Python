<script type="text/javascript">
      $(document).ready(function(){
          var num = 124
          var someString = "some string"
          // some_array = [num, 123, 12333, "an so on"]
          var someArray = [num, 9, 12333, "an so on"]
          var someBool = true // true
          $.each(someArray, function(index, obj){
              // console.log(index, obj)
              // 10 % 3  == 1
              // 9 % 3 == 0
              if ( obj %2 == 0 && someBool) {
                console.log(obj, "is even")
              } else if (obj%3 == 0 && someBool){
                console.log(obj, "by 3")
              } else {
                console.log(obj, "false and/or is not even")
              }
          })
      }) 
   </script>





<script type="text/javascript">
      $(document).ready(function(){
        // jquery is ready to roll
        // $(selector)
        // $('body').css("background-color", "red")
        var $description = $(".description")
        // $description.css("height", "300px").css("width", "250px")
        console.log($description.length) // if 1 then exists// print()
        console.log($description.css("height")) // print()
        console.log($description.height())
        // if currentElementHeight > builtInHeight
        // add $description.css("overflow", "scroll")
        setTimeout(function(){
            // $('body').css("background-color", "red")
            $('h1').css("color", "purple")
            $('h1:nth-child(2)').text("Hello again!")
            $('#header-3').text("Hello again header 3!")
            $(".header").css("background-color", "green").css("padding", "30px")
        }, 2000) // in ms
      })
   </script>







<script type="text/javascript">
      $(document).ready(function(){
        var $descriptionItems = $(".description")
        // console.log($descriptionItems.length) // 0, 1, 2
        $.each($descriptionItems, function(index, obj){
          var item = $(this) 
          var actualHeight = item[0].scrollHeight
          var shouldBeHeight = item.height()
          // console.log(actualHeight, shouldBeHeight)
          if (actualHeight > shouldBeHeight + 50){
            item.css("overflow-y", "scroll")
          }
          // console.log(index, item.height())
          // console.log(index, obj)
        })
        var header3 = $("#header-3")
        header3.click(function(event){
          var $this = $(this)
          console.log($this)
          console.log(event)
          window.location.href = 'http://www.google.com/'
        })
        var descriptionLinks = $(".description a")
        descriptionLinks.click(function(event){
          console.log(event)
          event.preventDefault()
          var $this = $(this)
          var href = $this.attr("href")
          console.log(href)
          alert(href)
          window.location.href =href
        })
      })
   </script>










 <script type="text/javascript">
    $(document).ready(function(){
      var contentForm = $(".new-content-form")
      contentForm.submit(function(event){
        event.preventDefault()
        var $this = $(this)
        //console.log(contentForm.serialize())
        var textAreaContent = $this.find('textarea')
        // console.log(textAreaContent.attr("name"))
        //console.log(textAreaContent.val())
        var formMethod = $this.attr("method") // contentForm.attr("method")
        var formAction = $this.attr("action")
        var data = {
            "content": textAreaContent.val(),
            "method": formMethod,
            "action": formAction
        }
        $('.formDataSubmitted').text(textAreaContent.val() + " method is " + formMethod)
        textAreaContent.val("")
        // $.ajax({
        //   url:
        //   method:
        //   data:
        // })
      })
    })
 </script>
