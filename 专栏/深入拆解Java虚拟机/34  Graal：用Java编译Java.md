<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>34  Graal：用Java编译Java.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么我们要学习Java虚拟机？.md">00 开篇词  为什么我们要学习Java虚拟机？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Java代码是怎么运行的？.md">01  Java代码是怎么运行的？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;Java的基本类型.md">02  Java的基本类型.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Java虚拟机是如何加载Java类的.md">03  Java虚拟机是如何加载Java类的.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;JVM是如何执行方法调用的？（上）.md">04  JVM是如何执行方法调用的？（上）.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;JVM是如何执行方法调用的？（下）.md">05  JVM是如何执行方法调用的？（下）.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;JVM是如何处理异常的？.md">06  JVM是如何处理异常的？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;JVM是如何实现反射的？.md">07  JVM是如何实现反射的？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;JVM是怎么实现invokedynamic的？（上）.md">08  JVM是怎么实现invokedynamic的？（上）.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;JVM是怎么实现invokedynamic的？（下）.md">09  JVM是怎么实现invokedynamic的？（下）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;Java对象的内存布局.md">10  Java对象的内存布局.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;垃圾回收（上）.md">11  垃圾回收（上）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;垃圾回收（下）.md">12  垃圾回收（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Java内存模型.md">13  Java内存模型.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;Java虚拟机是怎么实现synchronized的？.md">14  Java虚拟机是怎么实现synchronized的？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;Java语法糖与Java编译器.md">15  Java语法糖与Java编译器.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;即时编译（上）.md">16  即时编译（上）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;即时编译（下）.md">17  即时编译（下）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;即时编译器的中间表达形式.md">18  即时编译器的中间表达形式.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;Java字节码（基础篇）.md">19  Java字节码（基础篇）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;方法内联（上）.md">20  方法内联（上）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;方法内联（下）.md">21  方法内联（下）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;HotSpot虚拟机的intrinsic.md">22  HotSpot虚拟机的intrinsic.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;逃逸分析.md">23  逃逸分析.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;字段访问相关优化.md">24  字段访问相关优化.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;循环优化.md">25  循环优化.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;向量化.md">26  向量化.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;注解处理器.md">27  注解处理器.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;基准测试框架JMH（上）.md">28  基准测试框架JMH（上）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;基准测试框架JMH（下）.md">29  基准测试框架JMH（下）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;Java虚拟机的监控及诊断工具（命令行篇）.md">30  Java虚拟机的监控及诊断工具（命令行篇）.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;Java虚拟机的监控及诊断工具（GUI篇）.md">31  Java虚拟机的监控及诊断工具（GUI篇）.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;JNI的运行机制.md">32  JNI的运行机制.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;Java&#32;Agent与字节码注入.md">33  Java Agent与字节码注入.md</a>

                </li>
                <li>

                    <a class="current-tab" href="34&#32;&#32;Graal：用Java编译Java.md">34  Graal：用Java编译Java.md</a>
                    

                </li>
                <li>

                    
                    <a href="35&#32;&#32;Truffle：语言实现框架.md">35  Truffle：语言实现框架.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;SubstrateVM：AOT编译框架.md">36  SubstrateVM：AOT编译框架.md</a>

                </li>
                <li>

                    
                    <a href="尾声丨道阻且长，努力加餐.html.md">尾声丨道阻且长，努力加餐.html.md</a>

                </li>
                <li>

                    
                    <a href="工具篇&#32;&#32;常用工具介绍.md">工具篇  常用工具介绍.md</a>

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
                        <div><h1>34  Graal：用Java编译Java</h1>
<p>最后这三篇文章，我将介绍 Oracle Labs 的 GraalVM 项目。</p>
<p>GraalVM 是一个高性能的、支持多种编程语言的执行环境。它既可以在传统的 OpenJDK 上运行，也可以通过 AOT（Ahead-Of-Time）编译成可执行文件单独运行，甚至可以集成至数据库中运行。</p>
<p>除此之外，它还移除了编程语言之间的边界，并且支持通过即时编译技术，将混杂了不同的编程语言的代码编译到同一段二进制码之中，从而实现不同语言之间的无缝切换。</p>
<p>今天这一篇，我们就来讲讲 GraalVM 的基石 Graal 编译器。</p>
<p>在之前的篇章中，特别是介绍即时编译技术的第二部分，我们反反复复提到了 Graal 编译器。这是一个用 Java 写就的即时编译器，它从 Java 9u 开始便被集成自 JDK 中，作为实验性质的即时编译器。</p>
<p>Graal 编译器可以通过 Java 虚拟机参数<code>-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler</code>启用。当启用时，它将替换掉 HotSpot 中的 C2 编译器，并响应原本由 C2 负责的编译请求。</p>
<p>在今天的文章中，我将详细跟你介绍一下 Graal 与 Java 虚拟机的交互、Graal 和 C2 的区别以及 Graal 的实现细节。</p>
<h2>Graal 和 Java 虚拟机的交互</h2>
<p>我们知道，即时编译器是 Java 虚拟机中相对独立的模块，它主要负责接收 Java 字节码，并生成可以直接运行的二进制码。</p>
<p>具体来说，即时编译器与 Java 虚拟机的交互可以分为如下三个方面。</p>
<ol>
<li>响应编译请求；</li>
<li>获取编译所需的元数据（如类、方法、字段）和反映程序执行状态的 profile；</li>
<li>将生成的二进制码部署至代码缓存（code cache）里。</li>
</ol>
<p>即时编译器通过这三个功能组成了一个响应编译请求、获取编译所需的数据，完成编译并部署的完整编译周期。</p>
<p>传统情况下，即时编译器是与 Java 虚拟机紧耦合的。也就是说，对即时编译器的更改需要重新编译整个 Java 虚拟机。这对于开发相对活跃的 Graal 来说显然是不可接受的。</p>
<p>为了让 Java 虚拟机与 Graal 解耦合，我们引入了<a href="https://openjdk.java.net/jeps/243">Java 虚拟机编译器接口</a>（JVM Compiler Interface，JVMCI），将上述三个功能抽象成一个 Java 层面的接口。这样一来，在 Graal 所依赖的 JVMCI 版本不变的情况下，我们仅需要替换 Graal 编译器相关的 jar 包（Java 9 以后的 jmod 文件），便可完成对 Graal 的升级。</p>
<p>JVMCI 的作用并不局限于完成由 Java 虚拟机发出的编译请求。实际上，Java 程序可以直接调用 Graal，编译并部署指定方法。</p>
<p>Graal 的单元测试便是基于这项技术。为了测试某项优化是否起作用，原本我们需要反复运行某一测试方法，直至 Graal 收到由 Java 虚拟机发出针对该方法的编译请求，而现在我们可以直接指定编译该方法，并进行测试。我们下一篇将介绍的 Truffle 语言实现框架，同样也是基于这项技术的。</p>
<h2>Graal 和 C2 的区别</h2>
<p>Graal 和 C2 最为明显的一个区别是：Graal 是用 Java 写的，而 C2 是用 C++ 写的。相对来说，Graal 更加模块化，也更容易开发与维护，毕竟，连 C2 的作者 Cliff Click 大神都不想重蹈用 C++ 开发 Java 虚拟机的覆辙。</p>
<p>许多开发者会觉得用 C++ 写的 C2 肯定要比 Graal 快。实际上，在充分预热的情况下，Java 程序中的热点代码早已经通过即时编译转换为二进制码，在执行速度上并不亚于静态编译的 C++ 程序。</p>
<p>再者，即便是解释执行 Graal，也仅是会减慢编译效率，而并不影响编译结果的性能。</p>
<p>换句话说，如果 C2 和 Graal 采用相同的优化手段，那么它们的编译结果是一样的。所以，程序达到稳定状态（即不再触发新的即时编译）的性能，也就是峰值性能，将也是一样的。</p>
<p>由于 Java 语言容易开发维护的优势，我们可以很方便地将 C2 的新优化移植到 Graal 中。反之则不然，比如，在 Graal 中被证实有效的部分逃逸分析（partial escape analysis）至今未被移植到 C2 中。</p>
<p>Graal 和 C2 另一个优化上的分歧则是方法内联算法。相对来说，Graal 的内联算法对新语法、新语言更加友好，例如 Java 8 的 lambda 表达式以及 Scala 语言。</p>
<p>我们曾统计过数十个 Java 或 Scala 程序的峰值性能。总体而言，Graal 编译结果的性能要优于 C2。对于 Java 程序来说，Graal 的优势并不明显；对于 Scala 程序来说，Graal 的性能优势达到了 10%。</p>
<p>大规模使用 Scala 的 Twitter 便在他们的生产环境中部署了 Graal 编译器，并取得了 11% 的性能提升。（<a href="https://downloads.ctfassets.net/oxjq45e8ilak/6eh2A72b4IyWsWOIcig4K0/cbb664566fe86672d92ddfb210623920/Chris_Thalinger_Twitter_s_quest_for_a_wholly_Graal_runtime.pdf">Slides</a>, <a href="https://youtu.be/G-vlQaPMAxg?t=20m15s">Video</a>，该数据基于 GraalVM 社区版。）</p>
<h2>Graal 的实现</h2>
<p>Graal 编译器将编译过程分为前端和后端两大部分。前端用于实现平台无关的优化（如方法内联），以及小部分平台相关的优化；而后端则负责大部分的平台相关优化（如寄存器分配），以及机器码的生成。</p>
<p>在介绍即时编译技术时，我曾提到过，Graal 和 C2 都采用了 Sea-of-Nodes IR。严格来说，这里指的是 Graal 的前端，而后端采用的是另一种非 Sea-of-Nodes 的 IR。通常，我们将前端的 IR 称之为 High-level IR，或者 HIR；后端的 IR 则称之为 Low-level IR，或者 LIR。</p>
<p>Graal 的前端是由一个个单独的优化阶段（optimization phase）构成的。我们可以将每个优化阶段想象成一个图算法：它会接收一个规则的图，遍历图上的节点并做出优化，并且返回另一个规则的图。前端中的编译阶段除了少数几个关键的之外，其余均可以通过配置选项来开启或关闭。</p>
<p><img src="assets/d9772c569c25eabb7c2e7af53878e3b8.png" alt="img" /></p>
<p>Graal 编译器前端的优化阶段（局部）</p>
<blockquote>
<p>感兴趣的同学可以阅读 Graal repo 里配置这些编译优化阶段的源文件
<a href="https://github.com/oracle/graal/blob/master/compiler/src/org.graalvm.compiler.core/src/org/graalvm/compiler/core/phases/HighTier.java">HighTier.java</a>，<a href="https://github.com/oracle/graal/blob/master/compiler/src/org.graalvm.compiler.core/src/org/graalvm/compiler/core/phases/MidTier.java">MidTier.java</a>，以及<a href="https://github.com/oracle/graal/blob/master/compiler/src/org.graalvm.compiler.core/src/org/graalvm/compiler/core/phases/LowTier.java">LowTier.java</a>。</p>
</blockquote>
<p>我们知道，Graal 和 C2 都采用了激进的投机性优化手段（speculative optimization）。</p>
<p>通常，这些优化都基于某种假设（assumption）。当假设出错的情况下，Java 虚拟机会借助去优化（deoptimization）这项机制，从执行即时编译器生成的机器码切换回解释执行，在必要情况下，它甚至会废弃这份机器码，并在重新收集程序 profile 之后，再进行编译。</p>
<p>举个以前讲过的例子，类层次分析。在进行虚方法内联时（或者其他与类层次相关的优化），我们可能会发现某个接口仅有一个实现。</p>
<p>在即时编译过程中，我们可以假设在之后的执行过程中仍旧只有这一个实现，并根据这个假设进行编译优化。当之后加载了接口的另一实现时，我们便会废弃这份机器码。</p>
<p>Graal 与 C2 相比会更加激进。它从设计上便十分青睐这种基于假设的优化手段。在编译过程中，Graal 支持自定义假设，并且直接与去优化节点相关联。</p>
<p>当对应的去优化被触发时，Java 虚拟机将负责记录对应的自定义假设。而 Graal 在第二次编译同一方法时，便会知道该自定义假设有误，从而不再对该方法使用相同的激进优化。</p>
<p>Java 虚拟机的另一个能够大幅度提升性能的特性是 intrinsic 方法，我在之前的篇章中已经详细介绍过了。在 Graal 中，实现高性能的 intrinsic 方法也相对比较简单。Graal 提供了一种替换方法调用的机制，在解析 Java 字节码时会将匹配到的方法调用，替换成对另一个内部方法的调用，或者直接替换为特殊节点。</p>
<p>举例来说，我们可以把比较两个 byte 数组的方法<code>java.util.Arrays.equals(byte[],byte[])</code>替换成一个特殊节点，用来代表整个数组比较的逻辑。这样一来，当前编译方法所对应的图将被简化，因而其适用于其他优化的可能性也将提升。</p>
<h2>总结与实践</h2>
<p>Graal 是一个用 Java 写就的、并能够将 Java 字节码转换成二进制码的即时编译器。它通过 JVMCI 与 Java 虚拟机交互，响应由后者发出的编译请求、完成编译并部署编译结果。</p>
<p>对 Java 程序而言，Graal 编译结果的性能略优于 OpenJDK 中的 C2；对 Scala 程序而言，它的性能优势可达到 10%（企业版甚至可以达到 20%！）。这背后离不开 Graal 所采用的激进优化方式。</p>
<hr />
<p>今天的实践环节，你可以尝试使用附带 Graal 编译器的 JDK。在 Java 10，11 中，你可以通过添加虚拟机参数<code>-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler</code>来启用，或者下载我们部署在<a href="https://www.oracle.com/technetwork/oracle-labs/program-languages/downloads/index.html">Oracle OTN</a>上的基于 Java 8 的版本。</p>
<blockquote>
<p>在刚开始运行的过程中，Graal 编译器本身需要被即时编译，会抢占原本可用于编译应用代码的计算资源。因此，目前 Graal 编译器的启动性能会较差。最后一篇我会介绍解决方案。</p>
</blockquote>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="33&#32;&#32;Java&#32;Agent与字节码注入.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="35&#32;&#32;Truffle：语言实现框架.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4358306c6d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E6%8B%86%E8%A7%A3Java%E8%99%9A%E6%8B%9F%E6%9C%BA/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
