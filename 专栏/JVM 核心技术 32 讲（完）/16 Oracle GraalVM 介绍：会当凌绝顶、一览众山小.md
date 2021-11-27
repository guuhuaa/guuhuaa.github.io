<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 Oracle GraalVM 介绍：会当凌绝顶、一览众山小.md</title>
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

                    
                    <a href="01&#32;阅读此专栏的正确姿势.md">01 阅读此专栏的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;环境准备：千里之行，始于足下.md">02 环境准备：千里之行，始于足下.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;常用性能指标：没有量化，就没有改进.md">03 常用性能指标：没有量化，就没有改进.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;JVM&#32;基础知识：不积跬步，无以至千里.md">04 JVM 基础知识：不积跬步，无以至千里.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Java&#32;字节码技术：不积细流，无以成江河.md">05 Java 字节码技术：不积细流，无以成江河.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Java&#32;类加载器：山不辞土，故能成其高.md">06 Java 类加载器：山不辞土，故能成其高.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;Java&#32;内存模型：海不辞水，故能成其深.md">07 Java 内存模型：海不辞水，故能成其深.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;JVM&#32;启动参数详解：博观而约取、厚积而薄发.md">08 JVM 启动参数详解：博观而约取、厚积而薄发.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;JDK&#32;内置命令行工具：工欲善其事，必先利其器.md">09 JDK 内置命令行工具：工欲善其事，必先利其器.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;JDK&#32;内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md">10 JDK 内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;JDWP&#32;简介：十步杀一人，千里不留行.md">11 JDWP 简介：十步杀一人，千里不留行.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;JMX&#32;与相关工具：山高月小，水落石出.md">12 JMX 与相关工具：山高月小，水落石出.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;常见的&#32;GC&#32;算法（GC&#32;的背景与原理）.md">13 常见的 GC 算法（GC 的背景与原理）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;常见的&#32;GC&#32;算法（ParallelCMSG1）.md">14 常见的 GC 算法（ParallelCMSG1）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;Java11&#32;ZGC&#32;和&#32;Java12&#32;Shenandoah&#32;介绍：苟日新、日日新、又日新.md">15 Java11 ZGC 和 Java12 Shenandoah 介绍：苟日新、日日新、又日新.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;Oracle&#32;GraalVM&#32;介绍：会当凌绝顶、一览众山小.md">16 Oracle GraalVM 介绍：会当凌绝顶、一览众山小.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;GC&#32;日志解读与分析（基础配置）.md">17 GC 日志解读与分析（基础配置）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;GC&#32;日志解读与分析（实例分析上篇）.md">18 GC 日志解读与分析（实例分析上篇）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;GC&#32;日志解读与分析（实例分析中篇）.md">19 GC 日志解读与分析（实例分析中篇）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;GC&#32;日志解读与分析（实例分析下篇）.md">20 GC 日志解读与分析（实例分析下篇）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;GC&#32;日志解读与分析（番外篇可视化工具）.md">21 GC 日志解读与分析（番外篇可视化工具）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;JVM&#32;的线程堆栈等数据分析：操千曲而后晓声、观千剑而后识器.md">22 JVM 的线程堆栈等数据分析：操千曲而后晓声、观千剑而后识器.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;内存分析与相关工具上篇（内存布局与分析工具）.md">23 内存分析与相关工具上篇（内存布局与分析工具）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;内存分析与相关工具下篇（常见问题分析）.md">24 内存分析与相关工具下篇（常见问题分析）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;FastThread&#32;相关的工具介绍：欲穷千里目，更上一层楼.md">25 FastThread 相关的工具介绍：欲穷千里目，更上一层楼.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;面临复杂问题时的几个高级工具：它山之石，可以攻玉.md">26 面临复杂问题时的几个高级工具：它山之石，可以攻玉.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;JVM&#32;问题排查分析上篇（调优经验）.md">27 JVM 问题排查分析上篇（调优经验）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;JVM&#32;问题排查分析下篇（案例实战）.md">28 JVM 问题排查分析下篇（案例实战）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;GC&#32;疑难情况问题排查与分析（上篇）.md">29 GC 疑难情况问题排查与分析（上篇）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;GC&#32;疑难情况问题排查与分析（下篇）.md">30 GC 疑难情况问题排查与分析（下篇）.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;JVM&#32;相关的常见面试问题汇总：运筹策帷帐之中，决胜于千里之外.md">31 JVM 相关的常见面试问题汇总：运筹策帷帐之中，决胜于千里之外.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;应对容器时代面临的挑战：长风破浪会有时、直挂云帆济沧海.md">32 应对容器时代面临的挑战：长风破浪会有时、直挂云帆济沧海.md</a>

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
                        <div><h1>16 Oracle GraalVM 介绍：会当凌绝顶、一览众山小</h1>
<h3>GraalVM 简介与特性</h3>
<p>前面了解了那么多的 JVM 相关技术，我们可以发现一个脉络就是 Java 相关的体系越来越复杂，越来越强大。放眼看去，最近十年来，各种各类的技术和平台层出不穷，每类技术都有自己的适用场景和使用人群。并且伴随着微服务和云原生等理念的出现和发展，越来越多的技术被整合到一起。那么作为目前最流行的平台技术，Java/JVM 也自然不会在这个大潮中置身事外。本节我们介绍一个语言平台的集大成者 GraalVM：</p>
<ul>
<li>从功能的广度上，它的目标是打通各类不同的语言平台，这样开发者可以博取众长，不同的团队、不同的模块能够使用不同的平台去做。（这也是目前微服务架构的一个流行趋势。试想一下：一个非常大的产品线，大家共同维护几十个不同功能、各自独立部署运行的服务模块，那么每个团队就可以按照自己的想法选择合适的语言和平台工具去做。但是随着业务的不断发展，模块一直在重构，分分合合，怎么办？Python 的算法服务、Node.js 的 REST 脚手架，怎么跟 Java 的模块产生联系？！）</li>
<li>从性能的深度上，它则可以把各类程序转换成本地的原生应用，脱离中间语言和虚拟机来执行，从而获得最佳的性能，包括运行速度和内存占用。</li>
</ul>
<h4><strong>什么是 GraalVM</strong></h4>
<p>GraalVM 是 Oracle 开源的一款通用虚拟机产品，官方称之为 Universal GraalVM，是新一代的通用多语言高性能虚拟机。能执行各类高性能与互操作性任务，在无需额外开销的前提下允许用户构建多语言应用程序。</p>
<p>官方网站为：</p>
<blockquote>
<p><a href="https://www.graalvm.org/">https://www.graalvm.org</a></p>
</blockquote>
<h4><strong>GraalVM 有什么特点</strong></h4>
<p>GraalVM 既可以独立运行，也可以在不同的部署场景中使用，比如在 OpenJDK 虚拟机环境、Node.js 环境，或者 Oracle、MySQL 数据库等环境中运行。下图来自 GraalVM 官网，展示了目前支持的平台技术。</p>
<p><img src="assets/b255e7a0-5196-11ea-a2fb-85c45bbaa11c" alt="GraalVM system diagram" /></p>
<p>GraalVM 支持大量的语言，包括：</p>
<ul>
<li>基于 JVM 的语言（例如 Java、Scala、Groovy、Kotlin、Clojure 等）；</li>
<li>基于 LLVM 的语言（例如 C、C++ 等语言）；</li>
<li>动态语言，例如 JavaScript、Ruby、Python、R 语言等等。</li>
</ul>
<p>包括以下动态语言引擎：</p>
<ul>
<li>JavaScript 引擎：Graal.js 是一款 JavaScript 解释器/编译器，能够在 JVM 上运行 Node.js 应用；</li>
<li>FastR 引擎：这是 R 语言解释器/编译器；</li>
<li>RubyTruffle 引擎：支持 Ruby 且性能优于 Ruby。</li>
</ul>
<p>GraalVM 支持哪些特性呢？</p>
<ul>
<li>编译质量和执行性能更高，不管是 Java、Ruby 还是 R 语言，GraalVM 的编译器编译出来的代码，性能都更强悍</li>
<li>开发中可以组合 JavaScript、Java、Ruby 和 R 语言</li>
<li>在 GraalVM 上运行本地语言</li>
<li>开发适用于所有编程语言的通用工具</li>
<li>扩展基于 JVM 的应用程序</li>
<li>扩展本地应用程序</li>
<li>将 Java 程序编译之后作为本地库，供其他程序链接和调用</li>
<li>在数据库环境中支持多种语言，主要是 Oracle 和 MySQL 数据库环境</li>
<li>在 GraalVM 的基础上，我们甚至可以创建自己的语言</li>
<li>对于 Node.js 开发者来说，GraalVM 环境支持更大的堆内存，而且性能损失很小</li>
<li>程序的启动时间更短</li>
<li>占用内存更低</li>
</ul>
<p>启动时间对比：</p>
<p><img src="assets/0e6b5c50-5197-11ea-b2e1-7d26d62747f1" alt="microservices" /></p>
<p>占用内存对比：</p>
<p><img src="assets/16d152f0-5197-11ea-b2e1-7d26d62747f1" alt="microservices" /></p>
<h3>解决了哪些痛点</h3>
<p>GraalVM 提供了一个全面的生态系统，消除编程语言之间的隔离，打通了不同语言之间的鸿沟，在共享的运行时中实现了互操作性，让我们可以进行混合式多语言编程。</p>
<p>用 Graal 执行的语言可以互相调用，允许使用来自其他语言的库，提供了语言的互操作性。同时结合了对编译器技术的最新研究，在高负载场景下 GraalVM 的性能比传统 JVM 要好得多。</p>
<p>GraalVM 的混合式多语言编程可以解决开发中常见的这些问题：</p>
<ul>
<li>那个库我这个语言没有，我就不得不自己撸一个；</li>
<li>那个语言最适合解决我这个问题，但是我这个环境下跑不起来；</li>
<li>这个问题已经被我的语言解决了，但是我的语言跑起来太慢了；</li>
<li>通过使用 Polyglot API，GraalVM 要给开发者带来真正的语言级自由。</li>
</ul>
<p>开发人员使用自己最擅长的语言来编程，提高生产力的同时，更有希望赢得市场。</p>
<h4><strong>跨语言的工作原理</strong></h4>
<p>GraalVM 提供了一种在不同语言之间无缝传值的方法，而不需要像其它虚拟机一样进行序列化和反序列化。这样就保证了跨语言的零开销互操作性，也就是说性能无损失，所以才号称高性能虚拟机。</p>
<p>GraalVM 开发了“跨语言互操作协议”，它是一种特殊的接口协议，每种运行在 GraalVM 之上的语言都要实现这种协议，这样就能保证跨语言的互操作性。语言和语言之间无须了解对方就可以高效传值。该协议还在不断改进中，未来会支持更多特性。</p>
<p><strong>弱化主语言</strong></p>
<p>GraalVM 开发了一个实验性的启动器 Polyglot。在 Polyglot 里面不存在主语言的概念，每种语言都是平等的，可以使用 Polyglot 运行任意语言编写的程序，而不需要前面的每种语言单独一个启动器。Polyglot 会通过文件的扩展名来自动分类语言。</p>
<p><strong>Shell</strong></p>
<p>GraalVM 还开发了一个动态语言的 Shell，该 Shell 默认使用 JS 语言，可以使用命令切换到任意其它语言进行解释操作。</p>
<h4><strong>将 Java 程序编译为可执行文件</strong></h4>
<p>我们知道，Hotspot 推出之后，号称达到了 C++ 80% 的性能，其关键诀窍就在于 JIT 即时编译。</p>
<p>稍微推测一下，我们就会发现高性能的诀窍在于编译，而不是解释执行。</p>
<p>同样的道理，如果能够把 Java 代码编译为本地机器码，那么性能肯定也会有一个很大的提高。</p>
<p>恰好，GraalVM 就有静态编译的功能，可以把 Java 程序编译为本地二进制可执行文件。</p>
<p>GraalVM 可以为基于 JVM 的程序创建本地镜像。 镜像生成过程中，通过使用静态分析技术，从 Java main 方法开始，查找所有可以执行到的代码，然后执行全量的提前编译（AOT，ahead-of-time）。</p>
<p>生成的二进制可执行文件，包含整个程序的所有机器码指令，可以快速启动和执行，还可以被其他程序链接。</p>
<p>编译时还可以选择包含 GraalVM 编译器，以提供额外的即时（JIT）编译支持，从而高性能地运行任何基于 GraalVM 的语言。</p>
<p>为了获得额外的性能，还可以使用在应用程序的前一次运行中收集的配置文件引导优化来构建本机映像。下文可以看到如何构建本地映像的示例。</p>
<p>在 JVM 中运行应用程序需要启动过程，会消耗一定的时间，并且会额外占用一些内存。但通过静态编译之后的程序，相对来说占用内存更小、启动速度也更快。</p>
<h4><strong>GraalVM 组件</strong></h4>
<p>GraalVM 由核心组件和附加组件组成，打包在一起提供下载，GraalVM 当前最新版本是 19.3.1，是一款独立部署的 JDK。也包含一个共享的运行时，用于执行 Java 或基于 JVM 的语言（如 Scala、Kotlin）、动态语言（如 JavaScript、R、Ruby、Python）和基于 LLVM 的语言（如 C、C++）。</p>
<ul>
<li>运行时：主要是 Java 运行时系统和 NodeJS 运行时系统</li>
<li>库文件：比如编译器，JavaScript 解释器，LLVM 字节码（bitcode）执行器，Polyglot API 等。</li>
<li>工具：JavaScript REPL 环境、LLVM 相关的命令行工具、支持其他语言的安装程序。</li>
</ul>
<h3>下载与安装</h3>
<p>GraalVM 支持 Docker 容器，本文不进行介绍，相关信息请参考：</p>
<blockquote>
<p><a href="https://hub.docker.com/r/oracle/graalvm-ce/">https://hub.docker.com/r/oracle/graalvm-ce/</a></p>
</blockquote>
<p>下面我们来看看怎么在开发环境下载和安装。</p>
<p>\1. 打开官方网站：</p>
<blockquote>
<p><a href="https://www.graalvm.org/">https://www.graalvm.org/</a></p>
</blockquote>
<p>\2. 找到下载页面：</p>
<blockquote>
<p><a href="https://www.graalvm.org/downloads/">https://www.graalvm.org/downloads/</a></p>
</blockquote>
<p>从下载页面中可以看到，GraalVM 分为社区版和企业版两种版本。</p>
<p><strong>社区版（Community Edition）</strong></p>
<p>很明显，社区版是免费版本，提供基于 OpenJDK 8 和 OpenJDK 11 的版本，支持 x86 架构的 64 位系统：包括 macOS、Linux 和 Windows 平台。</p>
<p>需要从 GitHub 下载。下载页面为：</p>
<blockquote>
<p><a href="https://github.com/graalvm/graalvm-ce-builds/releases">https://github.com/graalvm/graalvm-ce-builds/releases</a></p>
</blockquote>
<p><strong>企业版（Enterprise Edition）</strong></p>
<p>企业版提供基于 Oracle Java 8 和 Oracle Java 11 的版本，主要支持 macOS 和 Linux 系统，Windows 系统的 GraalVM 企业版还是实验性质的开发者版本。</p>
<p>每个授权大约 1000~1500 人民币，当然，基于 Oracle 的习惯，大家是可以免费下载和试用的。</p>
<p>需要从 OTN（Oracle TechNetwork）下载：</p>
<blockquote>
<p><a href="https://www.oracle.com/technetwork/graalvm/downloads/index.html">https://www.oracle.com/technetwork/graalvm/downloads/index.html</a></p>
</blockquote>
<p>根据需要确定对应的版本，比如我们选择社区版。</p>
<p>社区版的组件包括：</p>
<ul>
<li>JVM</li>
<li>JavaScript Engine &amp; Node.js Runtime</li>
<li>LLVM Engine</li>
<li>Developer Tools</li>
</ul>
<p>从 <a href="https://github.com/graalvm/graalvm-ce-builds/releases">GitHub 下载页面</a> 中找到下载链接。</p>
<p>如下图所示：</p>
<p><img src="assets/cf68b260-519a-11ea-bb37-55480bd50c9e" alt="70802368.png" /></p>
<p>这里区分操作系统（macOS/darwin、Linux、Windows）、CPU 架构（AArch64、AMD64（Intel/AMD））、以及 JDK 版本。 我们根据自己的系统选择对应的下载链接。</p>
<p>比如 macOS 系统的 JDK 11 版本，对应的下载文件为：</p>
<pre><code># GraalVM 主程序绿色安装包
graalvm-ce-java11-darwin-amd64-19.3.1.tar.gz
# llvm-toolchain 的本地安装包；使用 gu -L 命令
llvm-toolchain-installable-java11-darwin-amd64-19.3.1.jar
# native-image 工具的本地安装包；使用 gu -L 命令
native-image-installable-svm-java11-darwin-amd64-19.3.1.jar

</code></pre>
<p>Windows 系统则只提供单个 zip 包下载：</p>
<pre><code># JDK11 版本
graalvm-ce-java11-windows-amd64-19.3.1.zip
# JDK8 版本
graalvm-ce-java8-windows-amd64-19.3.1.zip

</code></pre>
<p>然后右键另存为即可。</p>
<p>因为 GitHub 的某些资源可能被屏蔽，这里可能需要一点技巧。</p>
<p>如果下载不了，可以求助小伙伴，或者加入我们的交流群。或者试试下载 Oracle 的企业版，或者试试迅雷。</p>
<p>下载完成后进行解压，解压之后会发现这就是一个 JDK 的结构。</p>
<p>好吧，会使用 Java 的我，表示使用起来没什么压力。</p>
<p>进到解压后的 bin 目录，查看版本号：</p>
<pre><code># 注意这里是笔者的目录
cd graalvm-ce-java11-19.3.1/Contents/Home/bin/
# 看 Java 版本号
./java -version

openjdk version &quot;11.0.6&quot; 2020-01-14
OpenJDK Runtime Environment GraalVM CE 19.3.1 (build 11.0.6+9-jvmci-19.3-b07)
OpenJDK 64-Bit Server VM GraalVM CE 19.3.1 (build 11.0.6+9-jvmci-19.3-b07, mixed mode, sharing)

</code></pre>
<p>和 JDK 使用起来没多少差别，是吧？</p>
<p>如果是独立的环境，还可以执行设置 PATH 环境变量等操作。</p>
<p>解压后的 bin 目录下，除了 JDK 相关的可执行文件之外，还有：</p>
<ul>
<li>js 这个文件可以启动 JavaScript 控制台，类似于 Chrome 调试控制台一样的 REPL 环境。CTRL+C 退出。</li>
<li>node 这是嵌入的 Node.js，使用的是 GraalVM 的 JavaScript 引擎。</li>
<li>lli 官方说这是 GraalVM 集成的高性能 LLVM bitcode interpreter。</li>
<li>gu 全称是 GraalVM Updater，程序安装工具，比如可以安装 Python、R 和 Ruby 的语言包。</li>
</ul>
<h3>使用示例</h3>
<p>官方为各种语言提供了 GraalVM 相关的介绍和开发者文档：</p>
<ul>
<li><a href="https://www.graalvm.org/docs/reference-manual/languages/jvm/">Java 语言开发者文档</a></li>
<li><a href="https://www.graalvm.org/docs/reference-manual/languages/js/">Node.js 开发文档</a></li>
<li><a href="https://www.graalvm.org/docs/reference-manual/">Ruby、R 和 Python 开发者文档</a></li>
<li><a href="https://www.graalvm.org/docs/graalvm-as-a-platform/">工具开发和语言创造者文档</a></li>
</ul>
<h4><strong>Java 用法</strong></h4>
<p>下载并解压之后，只需要设置好 PATH，即可用于 Java 开发。</p>
<p>看官方的示例代码：</p>
<pre><code class="language-java">public class HelloWorld {
  public static void main(String[] args) {
    System.out.println(&quot;Hello, World!&quot;);
  }
}

</code></pre>
<p>这里为了省事，我们干点 stupid 的事情，读者理解意思即可，试验时也可以像我这样折腾。</p>
<pre><code class="language-shell"># 查看当前目录
$ pwd
/Users/renfufei/SOFT_ALL/graalvm-ce-java11-19.3.1/Contents/Home/bin

# 查看源文件
$ cat HelloWorld.java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println(&quot;Hello, World!&quot;);
  }
}

</code></pre>
<p>然后进行编译和执行：</p>
<pre><code class="language-shell"># 查看当前目录
$ pwd
/Users/renfufei/SOFT_ALL/graalvm-ce-java11-19.3.1/Contents/Home/bin

# 编译
$ ./javac HelloWorld.java

# 执行程序
$ ./java HelloWorld
Hello, World!

</code></pre>
<p>OK，程序正常输出。</p>
<p>更多示例请参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/examples/">https://www.graalvm.org/docs/examples/</a></p>
</blockquote>
<p>官方的示例还是很有意思的，对于提升我们的开发水平有一些帮助。</p>
<h4><strong>JS 的用法</strong></h4>
<p>执行 JS 的 REPL 调试环境：</p>
<pre><code class="language-shell">$ ./js
&gt; 1 + 1
2

</code></pre>
<p>想要退出，按 CTRL+C 即可。</p>
<p>查看 node 和 npm 的版本号：</p>
<pre><code>$ ./node -v
v12.14.0

$ ./npm -v
6.13.4

</code></pre>
<p>接下来就可以和正常的 Node.js 环境一样安装各种依赖包进行开发和使用了。</p>
<p>更多程序，请参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#running-javascript">https://www.graalvm.org/docs/getting-started/#running-javascript</a></p>
</blockquote>
<h4>LLVM 的用法</h4>
<p>根据官方的示例：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#running-llvm-bitcode">https://www.graalvm.org/docs/getting-started/#running-llvm-bitcode</a></p>
</blockquote>
<p>我们执行以下命令来安装 LLVM 相关工具：</p>
<pre><code class="language-shell">$ ./gu install llvm-toolchain
Downloading: Component catalog from www.graalvm.org
Processing Component: LLVM.org toolchain
Downloading: Component llvm-toolchain: LLVM.org toolchain from github.com
[                    ]

</code></pre>
<p>如果下载速度比较慢的话，这里得等好长时间，这里没有进度条显示，不要着急。</p>
<p>如果因为网络问题安装失败，也可以下载后使用本地的 jar 文件安装：</p>
<pre><code>./gu -L install ../lib/llvm-toolchain-installable-java11-darwin-amd64-19.3.1.jar

</code></pre>
<p>其中 <code>-L</code> 选项，等价于 <code>--local-file</code> 或者 <code>--file</code>，表示从本地文件安装组件。只要路径别填写错就行。</p>
<p>安装 <code>llvm-toolchain</code> 完成之后，查看安装路径，并配置到环境变量中：</p>
<pre><code class="language-shell">$ ./lli --print-toolchain-path
/Users/renfufei/SOFT_ALL/graalvm-ce-java11-19.3.1/Contents/Home/languages/llvm/native/bin

$ export LLVM_TOOLCHAIN=$(./lli --print-toolchain-path)

$ echo $LLVM_TOOLCHAIN
/Users/renfufei/SOFT_ALL/graalvm-ce-java11-19.3.1/Contents/Home/languages/llvm/native/bin

</code></pre>
<p>注意这里我偷懒，没配置 PATH，所以使用了 <code>./lli</code>。</p>
<p>创建一个 C 程序文件，内容示例如下：</p>
<pre><code>cat hello.c

#include &lt;stdio.h&gt;
int main() {
    printf(&quot;Hello from GraalVM!\n&quot;);
    return 0;
}

</code></pre>
<p>然后就可以编译和执行 bitcode 了：</p>
<pre><code class="language-shell"># 编译
$ $LLVM_TOOLCHAIN/clang hello.c -o hello

# 执行
$  ./lli hello
Hello from GraalVM!

</code></pre>
<h4><strong>安装其他工具和语言开发环境</strong></h4>
<p><strong>安装 Ruby</strong></p>
<p>安装文档请参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#running-ruby">https://www.graalvm.org/docs/getting-started/#running-ruby</a></p>
</blockquote>
<pre><code class="language-shell">./gu install ruby

</code></pre>
<p><strong>安装 R</strong></p>
<p>安装文档请参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#running-r">https://www.graalvm.org/docs/getting-started/#running-r</a></p>
</blockquote>
<pre><code class="language-shell">./gu install R

</code></pre>
<p><strong>安装 Python</strong></p>
<p>安装文档请参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#running-python">https://www.graalvm.org/docs/getting-started/#running-python</a></p>
</blockquote>
<pre><code class="language-shell">./gu install python

</code></pre>
<p>启动 Python：</p>
<pre><code class="language-shell">graalpython

</code></pre>
<p><strong>编译 Java 程序为可执行文件</strong></p>
<p>首先需要安装 native-image 工具，参考：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/reference-manual/native-image/#install-native-image">https://www.graalvm.org/docs/reference-manual/native-image/#install-native-image</a></p>
</blockquote>
<p>安装好之后就可以根据文档来使用了，就比如前面的 HelloWorld 程序。</p>
<pre><code class="language-java">// HelloWorld.java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println(&quot;Hello, World!&quot;);
  }
}

</code></pre>
<p>编译并执行：</p>
<pre><code class="language-shell"># Javac 编译
$ javac HelloWorld.java

# 编译为本地可执行程序
$ native-image HelloWorld

# 直接执行
$ ./helloworld
Hello, World!

</code></pre>
<p>看到这里，同学们可以不妨自己动手试试，把自己的 Spring Boot 之类的项目，用 GraalVM 打包成可执行文件（目前还不支持 Windows 版本）。再看一下启动时间，有惊喜哦。</p>
<p>参考文档：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/getting-started/#native-images">https://www.graalvm.org/docs/getting-started/#native-images</a></p>
</blockquote>
<p><strong>组合各种语言</strong></p>
<p>请参考文档：</p>
<blockquote>
<p><a href="https://www.graalvm.org/docs/reference-manual/polyglot/">https://www.graalvm.org/docs/reference-manual/polyglot/</a></p>
</blockquote>
<h3>参考资料</h3>
<ul>
<li><a href="https://www.ibm.com/developerworks/cn/java/j-use-graalvm-to-run-polyglot-apps/index.html">使用 GraalVM 开发多语言应用</a></li>
<li><a href="https://juejin.im/post/5ad7372f6fb9a045e511b0a4">全栈虚拟机 GraalVM 初体验</a></li>
<li><a href="https://www.oschina.net/p/graalvm">JVM 即时编译器 GraalVM</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;Java11&#32;ZGC&#32;和&#32;Java12&#32;Shenandoah&#32;介绍：苟日新、日日新、又日新.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;GC&#32;日志解读与分析（基础配置）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340e3891670ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/JVM%20%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%2032%20%E8%AE%B2%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
