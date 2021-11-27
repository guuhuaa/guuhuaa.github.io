<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  Context：你必须掌握的多线程并发控制神器.md</title>
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

                    <a class="current-tab" href="10&#32;&#32;Context：你必须掌握的多线程并发控制神器.md">10  Context：你必须掌握的多线程并发控制神器.md</a>
                    

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
                        <div><h1>10  Context：你必须掌握的多线程并发控制神器</h1>
<p>在上一节课中我留了一个作业，也就是让你自己练习使用 sync.Map，相信你已经做出来了。现在我为你讲解 sync.Map 的方法。</p>
<ol>
<li><strong>Store</strong>：存储一对 key-value 值。</li>
<li><strong>Load</strong>：根据 key 获取对应的 value 值，并且可以判断 key 是否存在。</li>
<li><strong>LoadOrStore</strong>：如果 key 对应的 value 存在，则返回该 value；如果不存在，存储相应的 value。</li>
<li><strong>Delete</strong>：删除一个 key-value 键值对。</li>
<li><strong>Range</strong>：循环迭代 sync.Map，效果与 for range 一样。</li>
</ol>
<p>相信有了这些方法的介绍，你对 sync.Map 会有更深入的理解。下面开始今天的课程：如何通过 Context 更好地控制并发。</p>
<h3>协程如何退出</h3>
<p>一个协程启动后，大部分情况需要等待里面的代码执行完毕，然后协程会自行退出。但是如果有一种情景，需要让协程提前退出怎么办呢？在下面的代码中，我做了一个监控狗用来监控程序：</p>
<p><em><strong>ch10/main.go</strong></em></p>
<pre><code>func main() {

   var wg sync.WaitGroup

   wg.Add(1)

   go func() {

      defer wg.Done()

      watchDog(&quot;【监控狗1】&quot;)

   }()

   wg.Wait()

}

func watchDog(name string){

   //开启for select循环，一直后台监控

   for{

      select {

      default:

         fmt.Println(name,&quot;正在监控……&quot;)

      }

      time.Sleep(1*time.Second)

   }

}
</code></pre>
<p>我通过 watchDog 函数实现了一个监控狗，它会一直在后台运行，每隔一秒就会打印&quot;监控狗正在监控……&quot;的文字。</p>
<p>如果需要让监控狗停止监控、退出程序，一个办法是定义一个全局变量，其他地方可以通过修改这个变量发出停止监控狗的通知。然后在协程中先检查这个变量，如果发现被通知关闭就停止监控，退出当前协程。</p>
<p>但是这种方法需要通过加锁来保证多协程下并发的安全，基于这个思路，有个升级版的方案：用 select+channel 做检测，如下面的代码所示：</p>
<p><em><strong>ch10/main.go</strong></em></p>
<pre><code>func main() {

   var wg sync.WaitGroup

   wg.Add(1)

   stopCh := make(chan bool) //用来停止监控狗

   go func() {

      defer wg.Done()

      watchDog(stopCh,&quot;【监控狗1】&quot;)

   }()

   time.Sleep(5 * time.Second) //先让监控狗监控5秒

   stopCh &lt;- true //发停止指令

   wg.Wait()

}

func watchDog(stopCh chan bool,name string){

   //开启for select循环，一直后台监控

   for{

      select {

      case &lt;-stopCh:

         fmt.Println(name,&quot;停止指令已收到，马上停止&quot;)

         return

      default:

         fmt.Println(name,&quot;正在监控……&quot;)

      }

      time.Sleep(1*time.Second)

   }

}
</code></pre>
<p>这个示例是使用 select+channel 的方式改造的 watchDog 函数，实现了通过 channel 发送指令让监控狗停止，进而达到协程退出的目的。以上示例主要有两处修改，具体如下：</p>
<ol>
<li>为 watchDog 函数增加 stopCh 参数，用于接收停止指令；</li>
<li>在 main 函数中，声明用于停止的 stopCh，传递给 watchDog 函数，然后通过 stopCh&lt;-true 发送停止指令让协程退出。</li>
</ol>
<h3>初识 Context</h3>
<p>以上示例是 select+channel 比较经典的使用场景，这里也顺便复习了 select 的知识。</p>
<p>通过 select+channel 让协程退出的方式比较优雅，但是如果我们希望做到同时取消很多个协程呢？如果是定时取消协程又该怎么办？这时候 select+channel 的局限性就凸现出来了，即使定义了多个 channel 解决问题，代码逻辑也会非常复杂、难以维护。</p>
<p>要解决这种复杂的协程问题，必须有一种可以跟踪协程的方案，只有跟踪到每个协程，才能更好地控制它们，这种方案就是 Go 语言标准库为我们提供的 Context，也是这节课的主角。</p>
<p>现在我通过 Context 重写上面的示例，实现让监控狗停止的功能，如下所示：</p>
<p><em><strong>ch10/main.go</strong></em></p>
<pre><code>func main() {

   var wg sync.WaitGroup

   wg.Add(1)

   ctx,stop:=context.WithCancel(context.Background())

   go func() {

      defer wg.Done()

      watchDog(ctx,&quot;【监控狗1】&quot;)

   }()

   time.Sleep(5 * time.Second) //先让监控狗监控5秒

   stop() //发停止指令

   wg.Wait()

}

func watchDog(ctx context.Context,name string) {

   //开启for select循环，一直后台监控

   for {

      select {

      case &lt;-ctx.Done():

         fmt.Println(name,&quot;停止指令已收到，马上停止&quot;)

         return

      default:

         fmt.Println(name,&quot;正在监控……&quot;)

      }

      time.Sleep(1 * time.Second)

   }

}
</code></pre>
<p>相比 select+channel 的方案，Context 方案主要有 4 个改动点。</p>
<ol>
<li>watchDog 的 stopCh 参数换成了 ctx，类型为 context.Context。</li>
<li>原来的 case &lt;-stopCh 改为 case &lt;-ctx.Done()，用于判断是否停止。</li>
<li>使用 context.WithCancel(context.Background()) 函数生成一个可以取消的 Context，用于发送停止指令。这里的 context.Background() 用于生成一个空 Context，一般作为整个 Context 树的根节点。</li>
<li>原来的 stopCh &lt;- true 停止指令，改为 context.WithCancel 函数返回的取消函数 stop()。</li>
</ol>
<p>可以看到，这和修改前的整体代码结构一样，只不过从 channel 换成了 Context。以上示例只是 Context 的一种使用场景，它的能力不止于此，现在我来介绍什么是 Context。</p>
<h2>什么是 Context</h2>
<p>一个任务会有很多个协程协作完成，一次 HTTP 请求也会触发很多个协程的启动，而这些协程有可能会启动更多的子协程，并且无法预知有多少层协程、每一层有多少个协程。</p>
<p>如果因为某些原因导致任务终止了，HTTP 请求取消了，那么它们启动的协程怎么办？该如何取消呢？因为取消这些协程可以节约内存，提升性能，同时避免不可预料的 Bug。</p>
<p>Context 就是用来简化解决这些问题的，并且是并发安全的。Context 是一个接口，它具备手动、定时、超时发出取消信号、传值等功能，主要用于控制多个协程之间的协作，尤其是取消操作。一旦取消指令下达，那么被 Context 跟踪的这些协程都会收到取消信号，就可以做清理和退出操作。</p>
<p>Context 接口只有四个方法，下面进行详细介绍，在开发中你会经常使用它们，你可以结合下面的代码来看。</p>
<pre><code>type Context interface {

   Deadline() (deadline time.Time, ok bool)

   Done() &lt;-chan struct{}

   Err() error

   Value(key interface{}) interface{}

}
</code></pre>
<ol>
<li>Deadline 方法可以获取设置的截止时间，第一个返回值 deadline 是截止时间，到了这个时间点，Context 会自动发起取消请求，第二个返回值 ok 代表是否设置了截止时间。</li>
<li>Done 方法返回一个只读的 channel，类型为 struct{}。在协程中，如果该方法返回的 chan 可以读取，则意味着 Context 已经发起了取消信号。通过 Done 方法收到这个信号后，就可以做清理操作，然后退出协程，释放资源。</li>
<li>Err 方法返回取消的错误原因，即因为什么原因 Context 被取消。</li>
<li>Value 方法获取该 Context 上绑定的值，是一个键值对，所以要通过一个 key 才可以获取对应的值。</li>
</ol>
<p>Context 接口的四个方法中最常用的就是 Done 方法，它返回一个只读的 channel，用于接收取消信号。当 Context 取消的时候，会关闭这个只读 channel，也就等于发出了取消信号。</p>
<h3>Context 树</h3>
<p>我们不需要自己实现 Context 接口，Go 语言提供了函数可以帮助我们生成不同的 Context，通过这些函数可以生成一颗 Context 树，这样 Context 才可以关联起来，父 Context 发出取消信号的时候，子 Context 也会发出，这样就可以控制不同层级的协程退出。</p>
<p>从使用功能上分，有四种实现好的 Context。</p>
<ol>
<li><strong>空 Context</strong>：不可取消，没有截止时间，主要用于 Context 树的根节点。</li>
<li><strong>可取消的 Context</strong>：用于发出取消信号，当取消的时候，它的子 Context 也会取消。</li>
<li><strong>可定时取消的 Context</strong>：多了一个定时的功能。</li>
<li><strong>值 Context</strong>：用于存储一个 key-value 键值对。</li>
</ol>
<p>从下图 Context 的衍生树可以看到，最顶部的是空 Context，它作为整棵 Context 树的根节点，在 Go 语言中，可以通过 context.Background() 获取一个根节点 Context。</p>
<p><img src="assets/CgqCHl_EyHOARbBqAAKzKmhclWo807.png" alt="Drawing 1.png" /></p>
<p>（四种 Context 的衍生树）</p>
<p>有了根节点 Context 后，这颗 Context 树要怎么生成呢？需要使用 Go 语言提供的四个函数。</p>
<ol>
<li><strong>WithCancel(parent Context)</strong>：生成一个可取消的 Context。</li>
<li><strong>WithDeadline(parent Context, d time.Time)</strong>：生成一个可定时取消的 Context，参数 d 为定时取消的具体时间。</li>
<li><strong>WithTimeout(parent Context, timeout time.Duration)</strong>：生成一个可超时取消的 Context，参数 timeout 用于设置多久后取消</li>
<li><strong>WithValue(parent Context, key, val interface{})</strong>：生成一个可携带 key-value 键值对的 Context。</li>
</ol>
<p>以上四个生成 Context 的函数中，前三个都属于可取消的 Context，它们是一类函数，最后一个是值 Context，用于存储一个 key-value 键值对。</p>
<h3>使用 Context 取消多个协程</h3>
<p>取消多个协程也比较简单，把 Context 作为参数传递给协程即可，还是以监控狗为例，如下所示：</p>
<p><em><strong>ch10/main.go</strong></em></p>
<pre><code>wg.Add(3)

go func() {

   defer wg.Done()

   watchDog(ctx,&quot;【监控狗2】&quot;)

}()

go func() {

   defer wg.Done()

   watchDog(ctx,&quot;【监控狗3】&quot;)

}()
</code></pre>
<p>示例中增加了两个监控狗，也就是增加了两个协程，这样一个 Context 就同时控制了三个协程，一旦 Context 发出取消信号，这三个协程都会取消退出。</p>
<p>以上示例中的 Context 没有子 Context，如果一个 Context 有子 Context，在该 Context 取消时会发生什么呢？下面通过一幅图说明：</p>
<p><img src="assets/Ciqc1F_EyIyAAO_TAADuPjzGt5U321.png" alt="Drawing 3.png" /></p>
<p>（Context 取消）</p>
<p>可以看到，当节点 Ctx2 取消时，它的子节点 Ctx4、Ctx5 都会被取消，如果还有子节点的子节点，也会被取消。也就是说根节点为 Ctx2 的所有节点都会被取消，其他节点如 Ctx1、Ctx3 和 Ctx6 则不会。</p>
<h3>Context 传值</h3>
<p>Context 不仅可以取消，还可以传值，通过这个能力，可以把 Context 存储的值供其他协程使用。我通过下面的代码来说明：</p>
<p><em><strong>ch10/main.go</strong></em></p>
<pre><code>func main() {

   wg.Add(4) //记得这里要改为4，原来是3，因为要多启动一个协程

   

  //省略其他无关代码

   valCtx:=context.WithValue(ctx,&quot;userId&quot;,2)

   go func() {

      defer wg.Done()

      getUser(valCtx)

   }()

   //省略其他无关代码

}

func getUser(ctx context.Context){

   for  {

      select {

      case &lt;-ctx.Done():

         fmt.Println(&quot;【获取用户】&quot;,&quot;协程退出&quot;)

         return

      default:

         userId:=ctx.Value(&quot;userId&quot;)

         fmt.Println(&quot;【获取用户】&quot;,&quot;用户ID为：&quot;,userId)

         time.Sleep(1 * time.Second)

      }

   }

}
</code></pre>
<p>这个示例是和上面的示例放在一起运行的，所以我省略了上面实例的重复代码。其中，通过 context.WithValue 函数存储一个 userId 为 2 的键值对，就可以在 getUser 函数中通过 ctx.Value(&quot;userId&quot;) 方法把对应的值取出来，达到传值的目的。</p>
<h3>Context 使用原则</h3>
<p>Context 是一种非常好的工具，使用它可以很方便地控制取消多个协程。在 Go 语言标准库中也使用了它们，比如 net/http 中使用 Context 取消网络的请求。</p>
<p>要更好地使用 Context，有一些使用原则需要尽可能地遵守。</p>
<ol>
<li>Context 不要放在结构体中，要以参数的方式传递。</li>
<li>Context 作为函数的参数时，要放在第一位，也就是第一个参数。</li>
<li>要使用 context.Background 函数生成根节点的 Context，也就是最顶层的 Context。</li>
<li>Context 传值要传递必须的值，而且要尽可能地少，不要什么都传。</li>
<li>Context 多协程安全，可以在多个协程中放心使用。</li>
</ol>
<p>以上原则是规范类的，Go 语言的编译器并不会做这些检查，要靠自己遵守。</p>
<h3>总结</h3>
<p>Context 通过 With 系列函数生成 Context 树，把相关的 Context 关联起来，这样就可以统一进行控制。一声令下，关联的 Context 都会发出取消信号，使用这些 Context 的协程就可以收到取消信号，然后清理退出。你在定义函数的时候，如果想让外部给你的函数发取消信号，就可以为这个函数增加一个 Context 参数，让外部的调用者可以通过 Context 进行控制，比如下载一个文件超时退出的需求。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;同步原语：sync&#32;包让你对并发控制得心应手.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;并发模式：Go&#32;语言中即学即用的高效并发模式.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433bf10dfa70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
