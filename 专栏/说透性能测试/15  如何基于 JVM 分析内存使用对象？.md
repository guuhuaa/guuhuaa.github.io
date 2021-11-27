<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15  如何基于 JVM 分析内存使用对象？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么每个测试人都要学好性能测试？.md">00 开篇词  为什么每个测试人都要学好性能测试？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;JMeter&#32;的核心概念.md">01  JMeter 的核心概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;JMeter&#32;参数化策略.md">02  JMeter 参数化策略.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建并执行&#32;JMeter&#32;脚本的正确姿势.md">03  构建并执行 JMeter 脚本的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">04  JMeter 二次开发其实并不难.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">05  如何基于 JMeter API 开发性能测试平台？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">06  Nginx 在系统架构中的作用.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;你真的知道如何制定性能测试的目标吗？.md">07  你真的知道如何制定性能测试的目标吗？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;性能测试场景的分类和意义.md">08  性能测试场景的分类和意义.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;如何制定一份有效的性能测试方案？.md">09  如何制定一份有效的性能测试方案？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;命令行监控&#32;Linux&#32;服务器的要点.md">10  命令行监控 Linux 服务器的要点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">11  分布式服务链路监控以及报警方案.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">12  如何把可视化监控也做得酷炫？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Docker&#32;的制作、运行以及监控.md">13  Docker 的制作、运行以及监控.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">14  如何从 CPU 飙升定位到热点方法？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;&#32;如何基于&#32;JVM&#32;分析内存使用对象？.md">15  如何基于 JVM 分析内存使用对象？.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">16  如何通过 Arthas 定位代码链路问题？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何应对&#32;Redis&#32;缓存穿透、击穿和雪崩？.md">17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何才能优化&#32;MySQL&#32;性能？.md">18  如何才能优化 MySQL 性能？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何根治慢&#32;SQL？.md">19  如何根治慢 SQL？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;线上全链路性能测试实践总结.md">20 结束语  线上全链路性能测试实践总结.md</a>

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
                        <div><h1>15  如何基于 JVM 分析内存使用对象？</h1>
<p>上一讲我带你学习了基于 JVM 的线程分析，相信你已经可以通过热点线程分析出哪些方法在消耗 CPU，拿到这些方法之后你就可以和研发人员讨论后续的优化方案了。那这一讲我们就来重点学习 JVM 内存是如何管理的，有哪些手段可以分析内存对象，并帮助你定位内存的瓶颈。</p>
<p>提到分析 JVM 的内存对象，可能你会问我，之前讲过如何判断服务器内存瓶颈，那 JVM 内存和服务器内存有什么联系呢。我们先来看下这两者的关系，如下图所示：</p>
<p><img src="assets/Cgp9HWA2u5SAFtvHAABjYpky-g8347.png" alt="图片3.png" /></p>
<p>图 1：内存关系示意图</p>
<p>其实二者的关系很简单，对于服务器系统而言，JVM 只是其中的一部分。当操作系统内存出现瓶颈时，我们便会重点排查哪些应用会占用内存。不过对于更深一步分析内存的使用，并不仅仅是统计使用、空闲等这些数值，我们需要进一步去了解内存结构，以及内存如何分配、如何回收，这样你才能更好地确定内存的问题。</p>
<h3>JVM 内存分配</h3>
<p>通过第 14 讲的学习你可以知道，Java 文件一般是先编译成 class 结尾的文件，然后通过类加载器到 JVM 内存中。接着我们来看看 JVM 内存结构图，这样能够对它有个全局的了解。</p>
<p><img src="assets/Cgp9HWA2u6iAHNxJAACTuTJQcko749.png" alt="图片1.png" /></p>
<p>图 2：JVM 内存分配示意图</p>
<h4>1.本地方法栈</h4>
<p>本地方法栈保存的是 native 方法的信息，native 方法就是 Java 调用非 Java 代码的接口，为什么会有这样的设置呢？简单来说，sun 的解释器是由 C 语言实现的，而 jre 又是基于 Java 语言，所以需要 native 方法来进行跨语言的调用。</p>
<h4>2.Java 栈</h4>
<p>Java 栈是常用的内存区域之一，它里面存放着<strong>基本数据类型</strong>和<strong>对象的引用</strong>，可能你不太清楚什么是对象的引用，拿上一讲中 HelloTester helloTester=new HelloTester() 为例，在 Java 栈中 HelloTester 是个引用，指向在堆空间中开辟的该对象的空间。</p>
<h4>3.方法区（JDK 1.8+已经移除）</h4>
<p>也叫作永久区，用来<strong>存储类信息</strong>，如上文描述的 HelloTester。值得注意的是方法区在 JDK 1.8 以上已经被元空间取代，并且元空间不在 JVM 中了，而是在本地内存中独立开辟存储空间。</p>
<h4>4.程序计数器</h4>
<p>可以认为是<strong>线程的信号指示器</strong>，它的作用是保存线程当前程序的执行位置，以保证多线程的切换。因为在多线程的情况下，CPU 并不是完成一个线程执行再去执行另外一个线程，而是不停地切换线程执行，这时程序计数器就可以发挥作用了。</p>
<h4>5.堆</h4>
<p>堆区域是 JVM 调优最重要的区域，堆中存放的数据很多是对象实例，如 HelloTester 的对象存储。堆空间占据着 JVM 中最大的存储区域，存放了很多对象，所以大多数基于 JVM 的内存调优也是对堆空间的调优。</p>
<p>堆空间并非取之不尽，如果一直存放总有用完的时候，所以对于有用的对象应当保存起来，无用的对象应当回收，为了更好地实现这一机制，JVM 将堆空间分成了新生代和老生代，如下图所示：</p>
<p><img src="assets/CioPOWA2vFqAaIvdAAChz7EIEu0014.png" alt="4.png" /></p>
<p>图 3：GC 示意对比图</p>
<p>通过图 3 可以看到新生代和老年代的对比，Minor GC 发生在新生代，而 Full GC 发生在老年代。新生代分为三个区，一个 Eden 区和两个 Survivor 区。</p>
<p>先来看下 Eden 区的作用，大部分新生成的对象都是在 Eden 区，Eden 区满了之后便没有内存给新对象使用，Eden 区便会 Minor GC 回收无用内存，剩下的存活对象便会转移到 Survivor 区。</p>
<p>那两个 Survivor 区的作用分别是什么呢？两者其实是对称分布的，一个是 From 区，一个是 To 区。从 Eden 区存活下来的对象首先会被复制到 From 区，当 From 区满时，此时还存活的对象会被转移到 To 区，经历了多次的 Minor GC 后，还存活的对象就会被复制到老年代，老年代的 GC 一般叫作 FullGC 或者 MajorGC。</p>
<p>我们对比下新生代垃圾回收和老年代垃圾回收的区别，如下表所示：</p>
<p><img src="assets/CioPOWA2vG2AJj5oAACm26T__YI787.png" alt="图片2.png" /></p>
<h3>如何定位内存占用问题</h3>
<p>回到我们实际工作当中，当你发现 JVM 中使用的内存越来越多或者增长很快的时候，频繁 GC 的时候，应当如何去定位哪些对象导致的这些问题呢？</p>
<p>这其实涉及两个问题：</p>
<ul>
<li>如何去观察 GC 的频次；</li>
<li>定位占用内存的对象。</li>
</ul>
<h4>1.如何观察 GC 的频次？</h4>
<p>本部分我以 JDK 自带的工具来讲解，我一般使用 jstat 来查看 GC 的频次。首先我们来看下基本用法，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6f1d00001b2f252b">[email&#160;protected]</a> ~]# jstat -gc 26607 1000 3

 S0C    S1C    S0U    S1U      EC       EU        OC         OU       MC     MU    CCSC   CCSU   YGC     YGCT    FGC    FGCT     GCT

512.0  512.0  320.0   0.0   86016.0  27828.5   175104.0   157974.6  122840.0 116934.9 16128.0 15060.4   5328   37.311   4      1.042   38.353

512.0  512.0  320.0   0.0   86016.0  27981.9   175104.0   157974.6  122840.0 116934.9 16128.0 15060.4   5328   37.311   4      1.042   38.353

512.0  512.0  320.0   0.0   86016.0  28885.4   175104.0   157974.6  122840.0 116934.9 16128.0 15060.4   5328   37.311   4      1.042   38.353
</code></pre>
<p>我们来解析下终端输入的命令：</p>
<pre><code>jstat -gc 26607 1000 3
</code></pre>
<ul>
<li>26607 代表查看的 PID 的 Java 进程号；</li>
<li>1000 代表每隔 1000ms 也就是 1s 显示一次；</li>
<li>3 代表一共显示三次。</li>
</ul>
<p>接着我们再来看输出选项代表的含义有哪些？这个输出的信息含量比较大，不过信息是有对应关系的，比如 S0C 和 S0U：</p>
<ul>
<li>一般 C 结尾的代表总的容量大小或者计数的次数；</li>
<li>U 结尾代表已使用的容量大小。</li>
</ul>
<p>这是通用的，你可以看到输出项中有很多以 C 或者 U 结尾。S0 则代表第一个 Survivor 区，也就是我上文说的 From 区。通过以上的讲解，我相信很多名词你不用死记硬背也能理解了，比如 S1C 和 S1U 则表示第二个 Survivor 区也就是 To 区的总容量和使用容量。</p>
<p>接下来我罗列下其他的输出选项含义。</p>
<ul>
<li>EC / EU：Eden 区的总容量/已使用空间的大小。</li>
<li>OC / OU：老年代总容量/老年代已使用空间大小。</li>
<li>MC / MU：方法区总容量/方法区已使用容量大小。</li>
<li>CCSC / CCSU：压缩类总容量/压缩类空间使用大小。</li>
<li>YGC / YGCT：年轻代垃圾回收的次数/年轻代垃圾回收消耗时间。</li>
<li>FGC / FGCT： 老年代垃圾回收次数/老年代垃圾回收消耗时间。</li>
<li>GCT：垃圾回收消耗总时间。</li>
</ul>
<p>这样对比着看会更直观一点，对于上述输出选项的含义我们都需要有一定的印象，从而通过垃圾回收频率和消耗时间初步判断 GC 是否存在可疑问题。</p>
<p>有同学问过这样的问题，<strong>堆内存区域划分了这么多代</strong>，感觉很复杂，为什么要这么做呢？</p>
<p>我想不分代，内存垃圾肯定也是可以回收的。而让内存区域分代，主要就是优化垃圾回收的性能，也就是 GC 的性能。有点类似于我们日常生活中的垃圾分类，你把干湿垃圾分离，一方面有利于下一步的再利用，再者对于我们后续垃圾的处理效率也会有较大的提升。对于内存回收其实也是这样的，如果不分代那么所有的对象可能都在同一个大的区间里，GC 依次判断则效率必然是很低，如果是分代处理，对不同的区域分以不同的回收策略，这样效率会高很多。</p>
<h4>2.如何定位占用内存的对象？</h4>
<p>这里我将推荐一个工具 jmap，通过 jmap 可以指定 Java 进程的 PID，查看该进程的对象、数量等等，接下来我做一个演示。</p>
<p>首先我们来查看进程号为 18658 的应用包，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ddafb2b2a99d9799">[email&#160;protected]</a> ~]# ps -ef|grep demo

root     18658     1  0 Dec09 ?后续省略
</code></pre>
<p>其中上述输出的第二列 18658 为进程号，然后将进程号通过命令组合可以查看以下信息：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="23514c4c57636967">[email&#160;protected]</a> ~]# jmap -histo 18658|head -n 20

 num     #instances         #bytes  class name

----------------------------------------------

   1:        157619       18840672  [C

   2:          8326        8324360  [B

   3:        146319        3511656  java.lang.String

   4:          9224        2825584  [I

   5:         65733        2103456  com.example.demo.entity.User

   6:         62508        2000256  java.util.HashMap$Node

   7:         21868        1618832  [Ljava.lang.Object;
</code></pre>
<ul>
<li>num 是编号；</li>
<li>instances 是生成的实例个数；</li>
<li>bytes 是实例占用的大小；</li>
<li>classs name 对象的类名。</li>
</ul>
<p>其中 [C、[S、[I、[B 对应的类型如下所示：</p>
<pre><code>[C is a char[]

[S is a short[]

[I is a int[]

[B is a byte[]
</code></pre>
<p>你注意下第五行，这是能够最直接看到的业务类，如果是业务对象尤其需要关注，看是否一直上升。</p>
<h3>可视化的 JVM 监控工具</h3>
<p>在第三模块中，你可以知道，对于监控定位我一般会采用命令行结合可视化的方案一并讲解，接下来我介绍一个 JDK 自带的 JVM 监控工具：jvisual。</p>
<p>jvisual 能做的事情很多，监控内存泄漏、跟踪垃圾回收、执行时内存分析、CPU 线程分析等，而且通过图形化的界面指引就可以完成，接下来我主要讲述 jvisual 如何使用以及如何看内存对象的占用。</p>
<p>先来看下 jvisual 是如何使用的，一般我们会在启动被测的 jar 服务里进行如下配置：</p>
<pre><code>nohup java -Djava.rmi.server.hostname=实际ip -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=1099 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -jar demo-0.0.1-SNAPSHOT.jar &amp;
</code></pre>
<p>通过这样的方式可以启动暴露 1099 端口，且连接时不需要认证。</p>
<p>然后在本机电脑 jdk 路径 bin 目录下找到 jvisualvm，双击打开，如下图所示：</p>
<p><img src="assets/Cgp9HWAze7uAY4i0AAIY8AO0bo0055.png" alt="Drawing 3.png" /></p>
<p>我们再配置相应的 jmx 连接，如下图所示：</p>
<p><img src="assets/CioPOWAze8GAEEsIAALCNqd4FCQ080.png" alt="Drawing 4.png" /></p>
<p>如果出现如下图所示的界面，就证明连接成功了。</p>
<p><img src="assets/Cgp9HWA2vMaASqv3AAJ2rG-zf3U45.jpeg" alt="image" /></p>
<p>这样我们就能够概览 JVM 的 CPU 和内存的使用情况，如下图所示，通过点击抽样器，你可以分别获得对象在 CPU 和内存的占用。值得注意的是很多初学者把这部分 CPU 监控或者内存监控认为是服务器硬件级别的，这是不对的，这些都是基于 JVM 的监控。</p>
<p><img src="assets/CioPOWAze9CAShx_AAG7jwD3hwI714.png" alt="Drawing 6.png" /></p>
<p>按照内存占用进行排序是非常清晰的，你可以看到随着性能测试的进行，User 类字节占用比例越来越高，如下图所示：</p>
<p><img src="assets/CioPOWAze9aAZifIAANlYUMJTPQ367.png" alt="Drawing 7.png" /></p>
<h3>总结</h3>
<p>通过本讲的学习，你了解了 JVM 的内存结构，知道了 Java 内存对象经常活动的区域，同时列举了常见的排查手段诊断内存问题。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435bac48f3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E8%AF%B4%E9%80%8F%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
