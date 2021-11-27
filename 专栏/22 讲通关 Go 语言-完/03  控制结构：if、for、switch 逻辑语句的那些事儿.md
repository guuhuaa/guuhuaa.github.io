<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03  控制结构：if、for、switch 逻辑语句的那些事儿.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词&#32;&#32;Go&#32;为开发者的需求设计，带你实现高效工作.md">00 开篇词  Go 为开发者的需求设计，带你实现高效工作.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;基础入门：编写你的第一个&#32;Go&#32;语言程序.md">01  基础入门：编写你的第一个 Go 语言程序.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;数据类型：你必须掌握的数据类型有哪些？.md">02  数据类型：你必须掌握的数据类型有哪些？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="03&#32;&#32;控制结构：if、for、switch&#32;逻辑语句的那些事儿.md">03  控制结构：if、for、switch 逻辑语句的那些事儿.md</a>
                    

                </li>
                <li>

                    
                    <a href="04&#32;&#32;集合类型：如何正确使用&#32;array、slice&#32;和&#32;map？.md">04  集合类型：如何正确使用 array、slice 和 map？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;函数和方法：Go&#32;语言中的函数和方法到底有什么不同？.md">05  函数和方法：Go 语言中的函数和方法到底有什么不同？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;struct&#32;和&#32;interface：结构体与接口都实现了哪些功能？.md">06  struct 和 interface：结构体与接口都实现了哪些功能？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;错误处理：如何通过&#32;error、deferred、panic&#32;等处理错误？.md">07  错误处理：如何通过 error、deferred、panic 等处理错误？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;并发基础：Goroutines&#32;和&#32;Channels&#32;的声明与使用.md">08  并发基础：Goroutines 和 Channels 的声明与使用.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;同步原语：sync&#32;包让你对并发控制得心应手.md">09  同步原语：sync 包让你对并发控制得心应手.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;Context：你必须掌握的多线程并发控制神器.md">10  Context：你必须掌握的多线程并发控制神器.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;并发模式：Go&#32;语言中即学即用的高效并发模式.md">11  并发模式：Go 语言中即学即用的高效并发模式.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;指针详解：在什么情况下应该使用指针？.md">12  指针详解：在什么情况下应该使用指针？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;参数传递：值、引用及指针之间的区别？.md">13  参数传递：值、引用及指针之间的区别？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;内存分配：new&#32;还是&#32;make？什么情况下该用谁？.md">14  内存分配：new 还是 make？什么情况下该用谁？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;运行时反射：字符串和结构体之间如何转换？.md">15  运行时反射：字符串和结构体之间如何转换？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;非类型安全：让你既爱又恨的&#32;unsafe.md">16  非类型安全：让你既爱又恨的 unsafe.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;SliceHeader：slice&#32;如何高效处理数据？.md">17  SliceHeader：slice 如何高效处理数据？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;质量保证：Go&#32;语言如何通过测试保证质量？.md">18  质量保证：Go 语言如何通过测试保证质量？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;性能优化：Go&#32;语言如何进行代码检查和优化？.md">19  性能优化：Go 语言如何进行代码检查和优化？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;协作开发：模块化管理为什么能够提升研发效能？.md">20  协作开发：模块化管理为什么能够提升研发效能？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;网络编程：Go&#32;语言如何玩转&#32;RESTful&#32;API&#32;服务？.md">21  网络编程：Go 语言如何玩转 RESTful API 服务？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;网络编程：Go&#32;语言如何通过&#32;RPC&#32;实现跨平台服务？.md">22  网络编程：Go 语言如何通过 RPC 实现跨平台服务？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;你的&#32;Go&#32;语言成长之路.md">23 结束语  你的 Go 语言成长之路.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>03  控制结构：if、for、switch 逻辑语句的那些事儿</h1>
<p>在上节课中我留了一个思考题，在一个字符串中查找另外一个字符串是否存在，这个其实是字符串查找的功能，假如我需要在“飞雪无情”这个字符串中查找“飞雪”，可以这么做：</p>
<pre><code>i:=strings.Index(&quot;飞雪无情&quot;,&quot;飞雪&quot;)
</code></pre>
<p>这就是 Go 语言标准库为我们提供的常用函数，以供我们使用，减少开发。</p>
<p>这节课我们继续讲解 Go 语言，今天的内容是：Go 语言代码逻辑的控制。</p>
<p>流程控制语句用于控制程序的执行顺序，这样你的程序就具备了逻辑结构。一般流程控制语句需要和各种条件结合使用，比如用于条件判断的 if，用于选择的 switch，用于循环的 for 等。这一节课，我会为你详细介绍，通过示例演示它们的使用方式。</p>
<h3>if 条件语句</h3>
<p>if 语句是条件语句，它根据布尔值的表达式来决定选择哪个分支执行：如果表达式的值为 true，则 if 分支被执行；如果表达式的值为 false，则 else 分支被执行。下面，我们来看一个 if 条件语句示例：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>func main() {

    i:=10

    if i &gt;10 {

        fmt.Println(&quot;i&gt;10&quot;)

    } else {

        fmt.Println(&quot;i&lt;=10&quot;)

    }

}
</code></pre>
<p>这是一个非常简单的 if……else 条件语句，当 i&gt;10 为 true 的时候，if 分支被执行，否则就执行 else 分支，你自己可以运行这段代码，验证打印结果。</p>
<p>关于 if 条件语句的使用有一些规则：</p>
<ol>
<li>if 后面的条件表达式不需要使用 ()，这和有些编程语言不一样，也更体现 Go 语言的简洁；</li>
<li>每个条件分支（if 或者 else）中的大括号是必须的，哪怕大括号里只有一行代码（如示例）；</li>
<li>if 紧跟的大括号 { 不能独占一行，else 前的大括号 } 也不能独占一行，否则会编译不通过；</li>
<li>在 if……else 条件语句中还可以增加多个 else if，增加更多的条件分支。</li>
</ol>
<p>通过 go run ch03/main.go 运行下面的这段代码，会看到输出了 5&lt;i&lt;=10 ，这说明代码中的 else if i&gt;5 &amp;&amp; i&lt;=10 成立，该分支被执行。</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>func main() {

    i:=6

    if i &gt;10 {

        fmt.Println(&quot;i&gt;10&quot;)

    } else if  i&gt;5 &amp;&amp; i&lt;=10 {

        fmt.Println(&quot;5&lt;i&lt;=10&quot;)

    } else {

        fmt.Println(&quot;i&lt;=5&quot;)

    }

}
</code></pre>
<p>你可以通过修改 i 的初始值，来验证其他分支的执行情况。</p>
<p>你还可以增加更多的 else if，以增加更多的条件分支，不过这种方式不被推荐，因为代码可读性差，多个条件分支可以使用我后面讲到的 switch 代替，使代码更简洁。</p>
<p>和其他编程语言不同，在 Go 语言的 if 语句中，可以有一个简单的表达式语句，并将该语句和条件语句使用分号 ; 分开。同样是以上的示例，我使用这种方式对其改造，如下面代码所示：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>func main() {

    if i:=6; i &gt;10 {

        fmt.Println(&quot;i&gt;10&quot;)

    } else if  i&gt;5 &amp;&amp; i&lt;=10 {

        fmt.Println(&quot;5&lt;i&lt;=10&quot;)

    } else {

        fmt.Println(&quot;i&lt;=5&quot;)

    }

}
</code></pre>
<p>在 if 关键字之后，i&gt;10 条件语句之前，通过分号 ; 分隔被初始化的 i:=6。这个简单语句主要用来在 if 条件判断之前做一些初始化工作，可以发现输出结果是一样的。</p>
<p>通过 if 简单语句声明的变量，只能在整个 if……else if……else 条件语句中使用，比如以上示例中的变量 i。</p>
<h3>switch 选择语句</h3>
<p>if 条件语句比较适合分支较少的情况，如果有很多分支的话，选择 switch 会更方便，比如以上示例，使用 switch 改造后的代码如下：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>switch i:=6;{

case i&gt;10:

    fmt.Println(&quot;i&gt;10&quot;)

case i&gt;5 &amp;&amp; i&lt;=10:

    fmt.Println(&quot;5&lt;i&lt;=10&quot;)

default:

    fmt.Println(&quot;i&lt;=5&quot;)

}
</code></pre>
<p>switch 语句同样也可以用一个简单的语句来做初始化，同样也是用分号 ; 分隔。每一个 case 就是一个分支，分支条件为 true 该分支才会执行，而且 case 分支后的条件表达式也不用小括号 () 包裹。</p>
<p>在 Go 语言中，switch 的 case 从上到下逐一进行判断，一旦满足条件，立即执行对应的分支并返回，其余分支不再做判断。也就是说 Go 语言的 switch 在默认情况下，case 最后自带 break。这和其他编程语言不一样，比如 C 语言在 case 分支里必须要有明确的 break 才能退出一个 case。Go 语言的这种设计就是为了防止忘记写 break 时，下一个 case 被执行。</p>
<p>那么如果你真的有需要，的确需要执行下一个紧跟的 case 怎么办呢？Go 语言也考虑到了，提供了 fallthrough 关键字。现在看个例子，如下面的代码所示：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>switch j:=1;j {

case 1:

    fallthrough

case 2:

    fmt.Println(&quot;1&quot;)

default:

    fmt.Println(&quot;没有匹配&quot;)

}
</code></pre>
<p>以上示例运行会输出 1，如果省略 case 1: 后面的 fallthrough，则不会有任何输出。</p>
<p>不知道你是否可以发现，和上一个例子对比，这个例子的 switch 后面是有表达式的，也就是输入了 ;j，而上一个例子的 switch 后只有一个用于初始化的简单语句。</p>
<p>当 switch 之后有表达式时，case 后的值就要和这个表达式的结果类型相同，比如这里的 j 是 int 类型，那么 case 后就只能使用 int 类型，如示例中的 case 1、case 2。如果是其他类型，比如使用 case &quot;a&quot; ，会提示类型不匹配，无法编译通过。</p>
<p>而对于 switch 后省略表达式的情况，整个 switch 结构就和 if……else 条件语句等同了。</p>
<p>switch 后的表达式也没有太多限制，是一个合法的表达式即可，也不用一定要求是常量或者整数。你甚至可以像如下代码一样，直接把比较表达式放在 switch 之后：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>switch 2&gt;1 {

case true:

    fmt.Println(&quot;2&gt;1&quot;)

case false:

    fmt.Println(&quot;2&lt;=1&quot;)

}
</code></pre>
<p>可见 Go 语言的 switch 语句非常强大且灵活。</p>
<h3>for 循环语句</h3>
<p>当需要计算 1 到 100 的数字之和时，如果用代码将一个个数字加起来，会非常复杂，可读性也不好，这就体现出循环语句的存在价值了。</p>
<p>下面是一个经典的 for 循环示例，从这个示例中，我们可以分析出 for 循环由三部分组成，其中，需要使用两个 ; 分隔，如下所示：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>sum:=0

for i:=1;i&lt;=100;i++ {

    sum+=i

}

fmt.Println(&quot;the sum is&quot;,sum)
</code></pre>
<p>其中：</p>
<ol>
<li>第一部分是一个简单语句，一般用于 for 循环的初始化，比如这里声明了一个变量，并对 i:=1 初始化；</li>
<li>第二部分是 for 循环的条件，也就是说，它表示 for 循环什么时候结束。这里的条件是 i&lt;=100；</li>
<li>第三部分是更新语句，一般用于更新循环的变量，比如这里 i++，这样才能达到递增循环的目的。</li>
</ol>
<p>需要特别留意的是，Go 语言里的 for 循环非常强大，以上介绍的三部分组成都不是必须的，可以被省略，下面我就来为你演示，省略以上三部分后的效果。</p>
<p>如果你以前学过其他编程语言，可能会见到 while 这样的循环语句，在 Go 语言中没有 while 循环，但是可以通过 for 达到 while 的效果，如以下代码所示：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>sum:=0

i:=1

for i&lt;=100 {

    sum+=i

    i++

}

fmt.Println(&quot;the sum is&quot;,sum)
</code></pre>
<p>这个示例和上面的 for 示例的效果是一样的，但是这里的 for 后只有 i&lt;=100 这一个条件语句，也就是说，它达到了 while 的效果。</p>
<p>在 Go 语言中，同样支持使用 continue、break 控制 for 循环：</p>
<ol>
<li>continue 可以跳出本次循环，继续执行下一个循环。</li>
<li>break 可以跳出整个 for 循环，哪怕 for 循环没有执行完，也会强制终止。</li>
</ol>
<p>现在我对上面计算 100 以内整数和的示例再进行修改，演示 break 的用法，如以下代码：</p>
<p><em><strong>ch03/main.go</strong></em></p>
<pre><code>sum:=0

i:=1

for {

    sum+=i

    i++

    if i&gt;100 {

        break

    }

}

fmt.Println(&quot;the sum is&quot;,sum)
</code></pre>
<p>这个示例使用的是没有任何条件的 for 循环，也称为 for 无限循环。此外，使用 break 退出无限循环，条件是 i&gt;100。</p>
<h3>总结</h3>
<p>这节课主要讲解 if、for 和 switch 这样的控制语句的基本用法，使用它们，你可以更好地控制程序的逻辑结构，达到业务需求的目的。</p>
<p>这节课的思考题是：任意举个例子，练习 for 循环 continue 的使用。</p>
<p>Go 语言提供的控制语句非常强大，本节课我并没有全部介绍，比如 switch 选择语句中的类型选择，for 循环语句中的 for range 等高级能力。这些高级能力我会在后面的课程中逐一介绍，接下来要讲的集合类型，就会详细地为你演示如何使用 for range 遍历集合，记得来听课！</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;&#32;数据类型：你必须掌握的数据类型有哪些？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;&#32;集合类型：如何正确使用&#32;array、slice&#32;和&#32;map？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433bc4892170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/22%20%E8%AE%B2%E9%80%9A%E5%85%B3%20Go%20%E8%AF%AD%E8%A8%80-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
