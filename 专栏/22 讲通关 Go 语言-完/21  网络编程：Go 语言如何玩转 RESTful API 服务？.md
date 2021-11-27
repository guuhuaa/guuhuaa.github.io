<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21  网络编程：Go 语言如何玩转 RESTful API 服务？.md</title>
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

                    
                    <a href="03&#32;&#32;控制结构：if、for、switch&#32;逻辑语句的那些事儿.md">03  控制结构：if、for、switch 逻辑语句的那些事儿.md</a>

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

                    <a class="current-tab" href="21&#32;&#32;网络编程：Go&#32;语言如何玩转&#32;RESTful&#32;API&#32;服务？.md">21  网络编程：Go 语言如何玩转 RESTful API 服务？.md</a>
                    

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
                        <div><h1>21  网络编程：Go 语言如何玩转 RESTful API 服务？</h1>
<p>从这一讲开始，我将带你学习本专栏的第五模块，在这个模块中，你将学到我们项目中最常用的编码操作，也就是编写 RESTful API 和 RPC 服务。在实际开发项目中，你编写的这些服务可以被其他服务使用，这样就组成了微服务的架构；也可以被前端调用，这样就可以前后端分离。</p>
<p>今天我就先来为你介绍什么是 RESTful API，以及 Go 语言是如何玩转 RESTful API 的。</p>
<h3>什么是 RESTful API</h3>
<p>RESTful API 是一套规范，它可以规范我们如何对服务器上的资源进行操作。在了解 RESTful API 之前，我先为你介绍下 HTTP Method，因为 RESTful API 和它是密不可分的。</p>
<p>说起 HTTP Method，最常见的就是<strong>POST</strong>和<strong>GET</strong>，其实最早在 HTTP 0.9 版本中，只有一个<strong>GET</strong>方法，该方法是一个<strong>幂等方法</strong>，用于获取服务器上的资源，也就是我们在浏览器中直接输入网址回车请求的方法。</p>
<p>在 HTTP 1.0 版本中又增加了<strong>HEAD</strong>和<strong>POST</strong>方法，其中常用的是 POST 方法，一般用于给服务端提交一个资源，导致服务器的资源发生变化。</p>
<p>随着网络越来越复杂，发现这两个方法是不够用的，就继续新增了方法。所以在 HTTP1.1 版本的时候，一口气增加到了 9 个，新增的方法有 HEAD、OPTIONS、PUT、DELETE、TRACE、PATCH 和 CONNECT。下面我为你一一介绍它们的作用。</p>
<ol>
<li>GET 方法可请求一个指定资源的表示形式，使用 GET 的请求应该只被用于获取数据。</li>
<li>HEAD 方法用于请求一个与 GET 请求的响应相同的响应，但没有响应体。</li>
<li>POST 方法用于将实体提交到指定的资源，通常导致服务器上的状态变化或副作用。</li>
<li>PUT 方法用于请求有效载荷替换目标资源的所有当前表示。</li>
<li>DELETE 方法用于删除指定的资源。</li>
<li>CONNECT 方法用于建立一个到由目标资源标识的服务器的隧道。</li>
<li>OPTIONS 方法用于描述目标资源的通信选项。</li>
<li>TRACE 方法用于沿着到目标资源的路径执行一个消息环回测试。</li>
<li>PATCH 方法用于对资源应用部分修改。</li>
</ol>
<p>从以上每个方法的介绍可以看到，HTTP 规范针对每个方法都给出了明确的定义，所以我们使用的时候也要尽可能地<strong>遵循这些定义</strong>，这样我们在开发中才可以更好地协作。</p>
<p>理解了这些 HTTP 方法，就可以更好地理解 RESTful API 规范了，因为 RESTful API 规范就是基于这些 HTTP 方法规范我们对服务器资源的操作，同时规范了 URL 的样式和 HTTP Status Code。</p>
<p>在 RESTful API 中，使用的主要是以下五种 HTTP 方法：</p>
<ol>
<li>GET，表示读取服务器上的资源；</li>
<li>POST，表示在服务器上创建资源；</li>
<li>PUT，表示更新或者替换服务器上的资源；</li>
<li>DELETE，表示删除服务器上的资源；</li>
<li>PATCH，表示更新 / 修改资源的一部分。</li>
</ol>
<p>以上 HTTP 方法在 RESTful API 规范中是一个操作，操作的就是服务器的资源，服务器的资源通过特定的 URL 表示。</p>
<p>现在我们通过一些示例让你更好地理解 RESTful API，如下所示：</p>
<pre><code>HTTP GET https://www.flysnow.org/users

HTTP GET https://www.flysnow.org/users/123
</code></pre>
<p>以上是两个 GET 方法的示例：</p>
<ul>
<li>第一个表示获取所有用户的信息；</li>
<li>第二个表示获取 ID 为 123 用户的信息。</li>
</ul>
<p>下面再看一个 POST 方法的示例，如下所示：</p>
<pre><code>HTTP POST https://www.flysnow.org/users
</code></pre>
<p>这个示例表示创建一个用户，通过 POST 方法给服务器提供创建这个用户所需的全部信息。</p>
<blockquote>
<p>注意：这里 users 是个复数。</p>
</blockquote>
<p>现在你已经知道了如何创建一个用户，那么如果要更新某个特定的用户怎么做呢？其实也非常简单，示例代码如下所示：</p>
<pre><code>HTTP PUT https://www.flysnow.org/users/123
</code></pre>
<p>这表示要更新 / 替换 ID 为 123 的这个用户，在更新的时候，会通过 PUT 方法提供更新这个用户需要的全部用户信息。这里 PUT 方法和 POST 方法不太一样的是，从 URL 上看，PUT 方法操作的是单个资源，比如这里 ID 为 123 的用户。</p>
<blockquote>
<p>小提示：如果要更新一个用户的部分信息，使用 PATCH 方法更恰当。</p>
</blockquote>
<p>看到这里，相信你已经知道了如何删除一个用户，示例代码如下所示：</p>
<pre><code>HTTP DELETE https://www.flysnow.org/users/123
</code></pre>
<p>DELETE 方法的使用和 PUT 方法一样，也是操作单个资源，这里是删除 ID 为 123 的这个用户。</p>
<h3>一个简单的 RESTful API</h3>
<p>相信你已经非常了解什么是 RESTful API 了，现在开始，我会带你通过一个使用 Golang 实现 RESTful API 风格的示例，加深 RESTful API 的理解。</p>
<p>Go 语言的一个很大的优势，就是可以很容易地开发出网络后台服务，而且性能快、效率高。在开发后端 HTTP 网络应用服务的时候，我们需要处理很多 HTTP 的请求访问，比如常见的RESTful API 服务，就要处理很多 HTTP 请求，然后把处理的信息返回给使用者。对于这类需求，Golang 提供了内置的 net/http 包帮我们处理这些 HTTP 请求，让我们可以比较方便地开发一个 HTTP 服务。</p>
<p>下面我们来看一个简单的 HTTP 服务的 Go 语言实现，代码如下所示：</p>
<p><em>ch21/main.go</em></p>
<pre><code>func main() {

   http.HandleFunc(&quot;/users&quot;,handleUsers)

   http.ListenAndServe(&quot;:8080&quot;, nil)

}

func handleUsers(w http.ResponseWriter, r *http.Request){

   fmt.Fprintln(w,&quot;ID:1,Name:张三&quot;)

   fmt.Fprintln(w,&quot;ID:2,Name:李四&quot;)

   fmt.Fprintln(w,&quot;ID:3,Name:王五&quot;)

}
</code></pre>
<p>这个示例运行后，你在浏览器中输入 http://localhost:8080/users, 就可以看到如下内容信息：</p>
<pre><code>ID:1,Name:张三

ID:2,Name:李四

ID:3,Name:王五
</code></pre>
<p>也就是获取所有的用户信息，但是这并不是一个 RESTful API，因为使用者不仅可以通过 HTTP GET 方法获得所有的用户信息，还可以通过 POST、DELETE、PUT 等 HTTP 方法获得所有的用户信息，这显然不符合 RESTful API 的规范。</p>
<p>现在我对以上示例进行修改，使它符合 RESTful API 的规范，修改后的示例代码如下所示：</p>
<p><em>ch20/main.go</em></p>
<pre><code>func handleUsers(w http.ResponseWriter, r *http.Request){

   switch r.Method {

   case &quot;GET&quot;:

      w.WriteHeader(http.StatusOK)

      fmt.Fprintln(w,&quot;ID:1,Name:张三&quot;)

      fmt.Fprintln(w,&quot;ID:2,Name:李四&quot;)

      fmt.Fprintln(w,&quot;ID:3,Name:王五&quot;)

   default:

      w.WriteHeader(http.StatusNotFound)

      fmt.Fprintln(w,&quot;not found&quot;)

   }

}
</code></pre>
<p>这里我只修改了 handleUsers 函数，在该函数中增加了只在使用 GET 方法时，才获得所有用户的信息，其他情况返回 not found。</p>
<p>现在再运行这个示例，会发现只能通过 HTTP GET 方法进行访问了，使用其他方法会提示 not found。</p>
<h3>RESTful JSON API</h3>
<p>在项目中最常见的是使用 JSON 格式传输信息，也就是我们提供的 RESTful API 要返回 JSON 内容给使用者。</p>
<p>同样用上面的示例，我把它改造成可以返回 JSON 内容的方式，示例代码如下所示：</p>
<p><em>ch20/main.go</em></p>
<pre><code>//数据源，类似MySQL中的数据

var users = []User{

   {ID: 1,Name: &quot;张三&quot;},

   {ID: 2,Name: &quot;李四&quot;},

   {ID: 3,Name: &quot;王五&quot;},

}

func handleUsers(w http.ResponseWriter, r *http.Request){

   switch r.Method {

   case &quot;GET&quot;:

      users,err:=json.Marshal(users)

      if err!=nil {

         w.WriteHeader(http.StatusInternalServerError)

         fmt.Fprint(w,&quot;{\&quot;message\&quot;: \&quot;&quot;+err.Error()+&quot;\&quot;}&quot;)

      }else {

         w.WriteHeader(http.StatusOK)

         w.Write(users)

      }

   default:

      w.WriteHeader(http.StatusNotFound)

      fmt.Fprint(w,&quot;{\&quot;message\&quot;: \&quot;not found\&quot;}&quot;)

   }

}

//用户

type User struct {

   ID int

   Name string

}
</code></pre>
<p>从以上代码可以看到，这次的改造主要是新建了一个 User 结构体，并且使用 users 这个切片存储所有的用户，然后在 handleUsers 函数中把它转化为一个 JSON 数组返回。这样，就实现了基于 JSON 数据格式的 RESTful API。</p>
<p>运行这个示例，在浏览器中输入 http://localhost:8080/users，可以看到如下信息：</p>
<pre><code>[{&quot;ID&quot;:1,&quot;Name&quot;:&quot;张三&quot;},{&quot;ID&quot;:2,&quot;Name&quot;:&quot;李四&quot;},{&quot;ID&quot;:3,&quot;Name&quot;:&quot;王五&quot;}]
</code></pre>
<p>这已经是 JSON 格式的用户信息，包含了所有用户。</p>
<h3>Gin 框架</h3>
<p>虽然 Go 语言自带的 net/http 包，可以比较容易地创建 HTTP 服务，但是它也有很多不足：</p>
<ul>
<li>不能单独地对请求方法（POST、GET 等）注册特定的处理函数；</li>
<li>不支持 Path 变量参数；</li>
<li>不能自动对 Path 进行校准；</li>
<li>性能一般；</li>
<li>扩展性不足；</li>
<li>……</li>
</ul>
<p>基于以上这些不足，出现了很多 Golang Web 框架，如 Mux，Gin、Fiber 等，今天我要为你介绍的就是这款使用最多的 Gin 框架。</p>
<h4>引入 Gin 框架</h4>
<p>Gin 框架是一个在 Github 上开源的 Web 框架，封装了很多 Web 开发需要的通用功能，并且性能也非常高，可以让我们很容易地写出 RESTful API。</p>
<p>Gin 框架其实是一个模块，也就是 Go Mod，所以采用 Go Mod 的方法引入即可。我在第 18讲的时候详细介绍过如何引入第三方的模块，这里再复习一下。</p>
<p>首先需要下载安装 Gin 框架，安装代码如下：</p>
<pre><code>$ go get -u github.com/gin-gonic/gin
</code></pre>
<p>然后就可以在 Go 语言代码中导入使用了，导入代码如下：</p>
<pre><code>import &quot;github.com/gin-gonic/gin&quot;
</code></pre>
<p>通过以上安装和导入这两个步骤，就可以在你的 Go 语言项目中使用 Gin 框架了。</p>
<h4>使用 Gin 框架</h4>
<p>现在，已经引入了 Gin 框架，下面我就是用 Gin 框架重写上面的示例，修改的代码如下所示：</p>
<p><em>ch21/main.go</em></p>
<pre><code>func main() {

   r:=gin.Default()

   r.GET(&quot;/users&quot;, listUser)

   r.Run(&quot;:8080&quot;)

}

func listUser(c *gin.Context)  {

   c.JSON(200,users)

}
</code></pre>
<p>相比 net/http 包，Gin 框架的代码非常简单，通过它的 GET 方法就可以创建一个只处理 HTTP GET 方法的服务，而且输出 JSON 格式的数据也非常简单，使用 c.JSON 方法即可。</p>
<p>最后通过 Run 方法启动 HTTP 服务，监听在 8080 端口。现在运行这个 Gin 示例，在浏览器中输入 http://localhost:8080/users，看到的信息和通过 net/http 包实现的效果是一样的。</p>
<h4>获取特定的用户</h4>
<p>现在你已经掌握了如何使用 Gin 框架创建一个简单的 RESTful API，并且可以返回所有的用户信息，那么如何获取特定用户的信息呢？</p>
<p>我们知道，如果要获得特定用户的信息，需要使用的是 GET 方法，并且 URL 格式如下所示：</p>
<pre><code>http://localhost:8080/users/2
</code></pre>
<p>以上示例中的 2 是用户的 ID，也就是通过 ID 来获取特定的用户。</p>
<p>下面我通过 Gin 框架 Path 路径参数来实现这个功能，示例代码如下：</p>
<p><em>ch21/main.go</em></p>
<pre><code>func main() {

   //省略没有改动的代码

   r.GET(&quot;/users/:id&quot;, getUser)

}

func getUser(c *gin.Context) {

   id := c.Param(&quot;id&quot;)

   var user User

   found := false

   //类似于数据库的SQL查询

   for _, u := range users {

      if strings.EqualFold(id, strconv.Itoa(u.ID)) {

         user = u

         found = true

         break

      }

   }

   if found {

      c.JSON(200, user)

   } else {

      c.JSON(404, gin.H{

         &quot;message&quot;: &quot;用户不存在&quot;,

      })

   }

}
</code></pre>
<p>在 Gin 框架中，路径中使用冒号表示 Path 路径参数，比如示例中的 :id，然后在 getUser 函数中可以通过 c.Param(&quot;id&quot;) 获取需要查询用户的 ID 值。</p>
<blockquote>
<p>小提示：Param 方法的参数要和 Path 路径参数中的一致，比如示例中都是 ID。</p>
</blockquote>
<p>现在运行这个示例，通过浏览器访问 <a href="http://localhost:8080/users/2">http://localhost:8080/users/2</a>，就可以获得 ID 为 2 的用户，输出信息如下所示：</p>
<pre><code>{&quot;ID&quot;:2,&quot;Name&quot;:&quot;李四&quot;}
</code></pre>
<p>可以看到，已经正确的获取到了 ID 为 2 的用户，他的名字叫李四。</p>
<p>假如我们访问一个不存在的 ID，会得到什么结果呢？比如 99，示例如下所示：</p>
<pre><code>➜ curl http://localhost:8080/users/99

{&quot;message&quot;:&quot;用户不存在&quot;}%
</code></pre>
<p>从以上示例输出可以看到，返回了『用户不存在』的信息，和我们代码中处理的逻辑一样。</p>
<h4>新增一个用户</h4>
<p>现在你已经可以使用 Gin 获取所有用户，还可以获取特定的用户，那么你也应该知道如何新增一个用户了，现在我通过 Gin 实现如何新增一个用户，看和你想的方案是否相似。</p>
<p>根据 RESTful API 规范，实现新增使用的是 POST 方法，并且 URL 的格式为 http://localhost:8080/users ，向这个 URL 发送数据，就可以新增一个用户，然后返回创建的用户信息。</p>
<p>现在我使用 Gin 框架实现新增一个用户，示例代码如下：</p>
<pre><code>func main() {

   //省略没有改动的代码

   r.POST(&quot;/users&quot;, createUser)

}

func createUser(c *gin.Context) {

   name := c.DefaultPostForm(&quot;name&quot;, &quot;&quot;)

   if name != &quot;&quot; {

      u := User{ID: len(users) + 1, Name: name}

      users = append(users, u)

      c.JSON(http.StatusCreated,u)

   } else {

      c.JSON(http.StatusOK, gin.H{

         &quot;message&quot;: &quot;请输入用户名称&quot;,

      })

   }

}
</code></pre>
<p>以上新增用户的主要逻辑是获取客户端上传的 name 值，然后生成一个 User 用户，最后把它存储到 users 集合中，达到新增用户的目的。</p>
<p>在这个示例中，使用 POST 方法来新增用户，所以只能通过 POST 方法才能新增用户成功。</p>
<p>现在运行这个示例，然后通过如下命令发送一个新增用户的请求，查看结果：</p>
<pre><code>➜ curl -X POST -d 'name=飞雪' http://localhost:8080/users

{&quot;ID&quot;:4,&quot;Name&quot;:&quot;飞雪&quot;}
</code></pre>
<p>可以看到新增用户成功，并且返回了新增的用户，还有分配的 ID。</p>
<h3>总结</h3>
<p>Go 语言已经给我们提供了比较强大的 SDK，让我们可以很容易地开发网络服务的应用，而借助第三方的 Web 框架，可以让这件事情更容易、更高效。比如这篇文章介绍的 Gin 框架，就可以很容易让我们开发出 RESTful API，更多关于 Gin 框架的使用可以参考 <a href="https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&amp;album_id=1362784031968149504&amp;__biz=MzI3MjU4Njk3Ng==#wechat_redirect">Golang Gin 实战</a>系列文章。</p>
<p>在我们做项目开发的时候，要善于借助已经有的轮子，让自己的开发更有效率，也更容易实现。
<img src="assets/Ciqc1F_1dACARBqrAAVSvK3wokw352.png" alt="go语言金句.png" />
在我们做项目开发的时候，会有增、删、改和查，现在增和查你已经学会了，那么就给你留 2 个作业，任选其中 1 个即可，它们是：</p>
<ol>
<li>修改一个用户的名字；</li>
<li>删除一个用户。</li>
</ol>
<p>下一讲，也就是本专栏的最后一讲，我将为你介绍如何使用 Go 语言实现 RPC 服务，记得来听课哦。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;&#32;协作开发：模块化管理为什么能够提升研发效能？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;&#32;网络编程：Go&#32;语言如何通过&#32;RPC&#32;实现跨平台服务？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433c3bff8b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
