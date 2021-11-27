<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  SliceHeader：slice 如何高效处理数据？.md</title>
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

                    <a class="current-tab" href="17&#32;&#32;SliceHeader：slice&#32;如何高效处理数据？.md">17  SliceHeader：slice 如何高效处理数据？.md</a>
                    

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
                        <div><h1>17  SliceHeader：slice 如何高效处理数据？</h1>
<p>在[第 4 讲|集合类型：如何正确使用 array、slice 和 map？]中，你已经学习了 slice（切片），并且知道如何使用。这节课我会详细介绍 slice 的原理，带你学习它的底层设计。</p>
<h3>数组</h3>
<p>在讲 slice 的原理之前，我先来介绍一下数组。几乎所有的编程语言里都存在数组，Go 也不例外。那么为什么 Go 语言除了数组之外又设计了 slice 呢？要想解答这个问题，我们先来了解数组的局限性。</p>
<p>在下面的示例中，a1、a2 是两个定义好的数组，但是它们的类型不一样。变量 a1 的类型是 [1]string，变量 a2 的类型是 [2]string，也就是说数组的大小属于数组类型的一部分，只有数组内部元素类型和大小一致时，这两个数组才是同一类型。</p>
<pre><code>a1:=[1]string{&quot;飞雪无情&quot;}

a2:=[2]string{&quot;飞雪无情&quot;}
</code></pre>
<p>可以总结为，一个数组由两部分构成：数组的大小和数组内的元素类型。</p>
<pre><code>//数组结构伪代码表示

array{

  len

  item type

}
</code></pre>
<p>比如变量 a1 的大小是 1，内部元素的类型是 string，也就是说 a1 最多只能存储 1 个类型为 string 的元素。而 a2 的大小是 2，内部元素的类型也是 string，所以 a2 最多可以存储 2 个类型为 string 的元素。<strong>一旦一个数组被声明，它的大小和内部元素的类型就不能改变</strong>，你不能随意地向数组添加任意多个元素。这是数组的第一个限制。</p>
<p>既然数组的大小是固定的，如果需要使用数组存储大量的数据，就需要提前指定一个合适的大小，比如 10 万，代码如下所示：</p>
<pre><code>a10:=[100000]string{&quot;飞雪无情&quot;}
</code></pre>
<p>这样虽然可以解决问题，但又带来了另外的问题，那就是内存占用。因为在 Go 语言中，函数间的传参是值传递的，数组作为参数在各个函数之间被传递的时候，同样的内容就会被一遍遍地复制，<strong>这就会造成大量的内存浪费</strong>，这是数组的第二个限制。</p>
<p>虽然数组有限制，但是它是 Go 非常重要的底层数据结构，比如 slice 切片的底层数据就存储在数组中。</p>
<h3>slice 切片</h3>
<p>你已经知道，数组虽然也不错，但是在操作上有不少限制，为了解决这些限制，Go 语言创造了 slice，也就是切片。切片是对数组的抽象和封装，它的底层是一个数组存储所有的元素，但是它可以动态地添加元素，容量不足时还可以自动扩容，你完全可以把切片理解为动态数组。在 Go 语言中，除了明确需要指定长度大小的类型需要数组来完成，大多数情况下都是使用切片的。</p>
<h4>动态扩容</h4>
<p>通过内置的 append 方法，你可以向一个切片中追加任意多个元素，所以这就可以解决数组的第一个限制。</p>
<p>在下面的示例中，我通过内置的 append 函数为切片 ss 添加了两个字符串，然后返回一个新的切片赋值给 ss。</p>
<pre><code>func main() {

   ss:=[]string{&quot;飞雪无情&quot;,&quot;张三&quot;}

   ss=append(ss,&quot;李四&quot;,&quot;王五&quot;)

   fmt.Println(ss)

}
</code></pre>
<p>现在运行这段代码，会看到如下打印结果：</p>
<pre><code>[飞雪无情 张三 李四 王五]
</code></pre>
<p>当通过 append 追加元素时，如果切片的容量不够，append 函数会自动扩容。比如上面的例子，我打印出使用 append 前后的切片长度和容量，代码如下：</p>
<pre><code>func main() {

   ss:=[]string{&quot;飞雪无情&quot;,&quot;张三&quot;}

   fmt.Println(&quot;切片ss长度为&quot;,len(ss),&quot;,容量为&quot;,cap(ss))

   ss=append(ss,&quot;李四&quot;,&quot;王五&quot;)

   fmt.Println(&quot;切片ss长度为&quot;,len(ss),&quot;,容量为&quot;,cap(ss))

   fmt.Println(ss)

}
</code></pre>
<p>其中，我通过内置的 len 函数获取切片的长度，通过 cap 函数获取切片的容量。运行这段代码，可以看到打印结果如下：</p>
<pre><code>切片ss长度为 2 ,容量为 2

切片ss长度为 4 ,容量为 4

[飞雪无情 张三 李四 王五]
</code></pre>
<p>在调用 append 之前，容量是 2，调用之后容量是 4，说明自动扩容了。</p>
<blockquote>
<p>小提示：append 自动扩容的原理是新创建一个底层数组，把原来切片内的元素拷贝到新数组中，然后再返回一个指向新数组的切片。</p>
</blockquote>
<h4>数据结构</h4>
<p>在 Go 语言中，切片其实是一个结构体，它的定义如下所示：</p>
<pre><code>type SliceHeader struct {

   Data uintptr

   Len  int

   Cap  int

}
</code></pre>
<p>SliceHeader 是切片在运行时的表现形式，它有三个字段 Data、Len 和 Cap。</p>
<ol>
<li>Data 用来指向存储切片元素的数组。</li>
<li>Len 代表切片的长度。</li>
<li>Cap 代表切片的容量。</li>
</ol>
<p>通过这三个字段，就可以把一个数组抽象成一个切片，便于更好的操作，所以不同切片对应的底层 Data 指向的可能是同一个数组。现在通过一个示例来证明，代码如下：</p>
<pre><code>func main() {

   a1:=[2]string{&quot;飞雪无情&quot;,&quot;张三&quot;}

   s1:=a1[0:1]

   s2:=a1[:]

   //打印出s1和s2的Data值，是一样的

   fmt.Println((*reflect.SliceHeader)(unsafe.Pointer(&amp;s1)).Data)

   fmt.Println((*reflect.SliceHeader)(unsafe.Pointer(&amp;s2)).Data)

}
</code></pre>
<p>用上节课学习的 unsafe.Pointer 把它们转换为 *reflect.SliceHeader 指针，就可以打印出 Data 的值，打印结果如下所示：</p>
<pre><code>824634150744

824634150744
</code></pre>
<p>你会发现它们是一样的，也就是这两个切片共用一个数组，所以我们在切片赋值、重新进行切片操作时，使用的还是同一个数组，没有复制原来的元素。这样可以减少内存的占用，提高效率。</p>
<blockquote>
<p>注意：多个切片共用一个底层数组虽然可以减少内存占用，但是如果有一个切片修改内部的元素，其他切片也会受影响。所以在切片作为参数在函数间传递的时候要小心，尽可能不要修改原切片内的元素。</p>
</blockquote>
<p>切片的本质是 SliceHeader，又因为函数的参数是值传递，所以传递的是 SliceHeader 的副本，而不是底层数组的副本。这时候切片的优势就体现出来了，因为 SliceHeader 的副本内存占用非常少，即使是一个非常大的切片（底层数组有很多元素），也顶多占用 24 个字节的内存，这就解决了大数组在传参时内存浪费的问题。</p>
<blockquote>
<p>小提示：SliceHeader 三个字段的类型分别是 uintptr、int 和 int，在 64 位的机器上，这三个字段最多也就是 int64 类型，一个 int64 占 8 个字节，三个 int64 占 24 个字节内存。</p>
</blockquote>
<p>要获取切片数据结构的三个字段的值，也可以不使用 SliceHeader，而是完全自定义一个结构体，只要字段和 SliceHeader 一样就可以了。</p>
<p>比如在下面的示例中，通过 unsfe.Pointer 转换成自定义的 *slice 指针，同样可以获取三个字段对应的值，你甚至可以把字段的名称改为 d、l 和 c，也可以达到目的。</p>
<pre><code>sh1:=(*slice)(unsafe.Pointer(&amp;s1))

fmt.Println(sh1.Data,sh1.Len,sh1.Cap)

type slice struct {

   Data uintptr

   Len  int

   Cap  int

}
</code></pre>
<blockquote>
<p>小提示：我们还是尽可能地用 SliceHeader，因为这是 Go 语言提供的标准，可以保持统一，便于理解。</p>
</blockquote>
<h4>高效的原因</h4>
<p>如果从集合类型的角度考虑，数组、切片和 map 都是集合类型，因为它们都可以存放元素，但是数组和切片的取值和赋值操作要更高效，因为它们是连续的内存操作，通过索引就可以快速地找到元素存储的地址。</p>
<p><img src="assets/Ciqc1F_i6yGAXy-tAAV617lfKek460.png" alt="金句.png" /></p>
<blockquote>
<p>小提示：当然 map 的价值也非常大，因为它的 Key 可以是很多类型，比如 int、int64、string 等，但是数组和切片的索引只能是整数。</p>
</blockquote>
<p>进一步对比，在数组和切片中，切片又是高效的，因为它在赋值、函数传参的时候，并不会把所有的元素都复制一遍，而只是复制 SliceHeader 的三个字段就可以了，共用的还是同一个底层数组。</p>
<p>在下面的示例中，我定义了两个函数 arrayF 和 sliceF，分别打印传入的数组和切片底层对应的数组指针。</p>
<pre><code>func main() {

   a1:=[2]string{&quot;飞雪无情&quot;,&quot;张三&quot;}

   fmt.Printf(&quot;函数main数组指针：%p\n&quot;,&amp;a1)

   arrayF(a1)

   s1:=a1[0:1]

   fmt.Println((*reflect.SliceHeader)(unsafe.Pointer(&amp;s1)).Data)

   sliceF(s1)

}

func arrayF(a [2]string){

   fmt.Printf(&quot;函数arrayF数组指针：%p\n&quot;,&amp;a)

}

func sliceF(s []string){

   fmt.Printf(&quot;函数sliceF Data：%d\n&quot;,(*reflect.SliceHeader)(unsafe.Pointer(&amp;s)).Data)

}
</code></pre>
<p>然后我在 main 函数里调用它们，运行程序会打印如下结果：</p>
<pre><code>函数main数组指针：0xc0000a6020

函数arrayF数组指针：0xc0000a6040

824634400800

函数sliceF Data：824634400800
</code></pre>
<p>你会发现，同一个数组在 main 函数中的指针和在 arrayF 函数中的指针是不一样的，这说明数组在传参的时候被复制了，又产生了一个新数组。而 slice 切片的底层 Data 是一样的，这说明不管是在 main 函数还是 sliceF 函数中，这两个切片共用的还是同一个底层数组，底层数组并没有被复制。</p>
<blockquote>
<p>小提示：切片的高效还体现在 for range 循环中，因为循环得到的临时变量也是个值拷贝，所以在遍历大的数组时，切片的效率更高。</p>
</blockquote>
<p><strong>切片基于指针的封装是它效率高的根本原因，因为可以减少内存的占用，以及减少内存复制时的时间消耗。</strong></p>
<h4>string 和 []byte 互转</h4>
<p>下面我通过 string 和 []byte 相互强制转换的例子，进一步帮你理解 slice 高效的原因。</p>
<p>比如我把一个 []byte 转为一个 string 字符串，然后再转换回来，示例代码如下：</p>
<pre><code>s:=&quot;飞雪无情&quot;

b:=[]byte(s)

s3:=string(b)

fmt.Println(s,string(b),s3)
</code></pre>
<p>在这个示例中，变量 s 是一个 string 字符串，它可以通过 []byte(s) 被强制转换为 []byte 类型的变量 b，又可以通过 string(b) 强制转换为 string 类型的变量 s3。打印它们三个变量的值，都是</p>
<p>“飞雪无情”。</p>
<p>Go 语言通过先分配一个内存再复制内容的方式，实现 string 和 []byte 之间的强制转换。现在我通过 string 和 []byte 指向的真实内容的内存地址，来验证强制转换是采用重新分配内存的方式。如下面的代码所示：</p>
<pre><code>s:=&quot;飞雪无情&quot;

fmt.Printf(&quot;s的内存地址：%d\n&quot;, (*reflect.StringHeader)(unsafe.Pointer(&amp;s)).Data)

b:=[]byte(s)

fmt.Printf(&quot;b的内存地址：%d\n&quot;,(*reflect.SliceHeader)(unsafe.Pointer(&amp;b)).Data)

s3:=string(b)

fmt.Printf(&quot;s3的内存地址：%d\n&quot;, (*reflect.StringHeader)(unsafe.Pointer(&amp;s3)).Data)
</code></pre>
<p>运行它们，你会发现打印出的内存地址都不一样，这说明虽然内容相同，但已经不是同一个字符串了，因为内存地址不同。</p>
<blockquote>
<p>小提示：你可以通过查看 runtime.stringtoslicebyte 和 runtime.slicebytetostring 这两个函数的源代码，了解关于 string 和 []byte 类型互转的具体实现。</p>
</blockquote>
<p>通过以上的示例代码，你已经知道了 SliceHeader 是什么。其实 StringHeader 和 SliceHeader 一样，代表的是字符串在程序运行时的真实结构，StringHeader 的定义如下所示：</p>
<pre><code>// StringHeader is the runtime representation of a string.

type StringHeader struct {

   Data uintptr

   Len  int

}
</code></pre>
<p>也就是说，在程序运行的时候，字符串和切片本质上就是 StringHeader 和 SliceHeader。这两个结构体都有一个 Data 字段，用于存放指向真实内容的指针。所以我们打印出 Data 这个字段的值，就可以判断 string 和 []byte 强制转换后是不是重新分配了内存。</p>
<p>现在你已经知道了 []byte(s) 和 string(b) 这种强制转换会重新拷贝一份字符串，如果字符串非常大，由于内存开销大，对于有高性能要求的程序来说，这种方式就无法满足了，需要进行性能优化。</p>
<p>如何优化呢？既然是因为内存分配导致内存开销大，那么优化的思路应该是在不重新申请内存的情况下实现类型转换。</p>
<p>仔细观察 StringHeader 和 SliceHeader 这两个结构体，会发现它们的前两个字段一模一样，那么 []byte 转 string，就等于通过 unsafe.Pointer 把 *SliceHeader 转为 *StringHeader，也就是 *[]byte 转 *string，原理和我上面讲的把切片转换成一个自定义的 slice 结构体类似。</p>
<p>在下面的示例中，s4 和 s3 的内容是一样的。不一样的是 s4 没有申请新内存（零拷贝），它和变量 b 使用的是同一块内存，因为它们的底层 Data 字段值相同，这样就节约了内存，也达到了 []byte 转 string 的目的。</p>
<pre><code>s:=&quot;飞雪无情&quot;

b:=[]byte(s)

//s3:=string(b)

s4:=*(*string)(unsafe.Pointer(&amp;b))
</code></pre>
<p>SliceHeader 有 Data、Len、Cap 三个字段，StringHeader 有 Data、Len 两个字段，所以 *SliceHeader 通过 unsafe.Pointer 转为 *StringHeader 的时候没有问题，因为 *SliceHeader 可以提供 *StringHeader 所需的 Data 和 Len 字段的值。但是反过来却不行了，因为 *StringHeader 缺少 *SliceHeader 所需的 Cap 字段，需要我们自己补上一个默认值。</p>
<p>在下面的示例中，b1 和 b 的内容是一样的，不一样的是 b1 没有申请新内存，而是和变量 s 使用同一块内存，因为它们底层的 Data 字段相同，所以也节约了内存。</p>
<pre><code>s:=&quot;飞雪无情&quot;

//b:=[]byte(s)

sh:=(*reflect.SliceHeader)(unsafe.Pointer(&amp;s))

sh.Cap = sh.Len

b1:=*(*[]byte)(unsafe.Pointer(sh))
</code></pre>
<blockquote>
<p>注意：通过 unsafe.Pointer 把 string 转为 []byte 后，不能对 []byte 修改，比如不可以进行 b1[0]=12 这种操作，会报异常，导致程序崩溃。这是因为在 Go 语言中 string 内存是只读的。</p>
</blockquote>
<p>通过 unsafe.Pointer 进行类型转换，避免内存拷贝提升性能的方法在 Go 语言标准库中也有使用，比如 strings.Builder 这个结构体，它内部有 buf 字段存储内容，在通过 String 方法把 []byte 类型的 buf 转为 string 的时候，就使用 unsafe.Pointer 提高了效率，代码如下：</p>
<pre><code>// String returns the accumulated string.

func (b *Builder) String() string {

   return *(*string)(unsafe.Pointer(&amp;b.buf))

}
</code></pre>
<p>string 和 []byte 的互转就是一个很好的利用 SliceHeader 结构体的示例，通过它可以实现零拷贝的类型转换，提升了效率，避免了内存浪费。</p>
<h3>总结</h3>
<p>通过 slice 切片的分析，相信你可以更深地感受 Go 的魅力，它把底层的指针、数组等进行封装，提供一个切片的概念给开发者，这样既可以方便使用、提高开发效率，又可以提高程序的性能。</p>
<p>Go 语言设计切片的思路非常有借鉴意义，你也可以使用 uintptr 或者 slice 类型的字段来提升性能，就像 Go 语言 SliceHeader 里的 Data uintptr 字段一样。</p>
<p>在这节课的最后，给你留一个思考题：你还可以找到哪些通过 unsafe.Pointer、uintptr 提升性能的例子呢？欢迎留言讨论。</p>
<p>下节课我们将进入工程管理模块，首先学习“质量保证：Go 语言如何通过测试保证质量？”记得来听课！</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;非类型安全：让你既爱又恨的&#32;unsafe.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;质量保证：Go&#32;语言如何通过测试保证质量？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433c24af5e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
