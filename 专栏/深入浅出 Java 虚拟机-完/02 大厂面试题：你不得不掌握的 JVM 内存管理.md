<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 大厂面试题：你不得不掌握的 JVM 内存管理.md</title>
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

                    
                    <a href="00&#32;开篇词：JVM，一块难啃的骨头.md">00 开篇词：JVM，一块难啃的骨头.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;一探究竟：为什么需要&#32;JVM？它处在什么位置？.md">01 一探究竟：为什么需要 JVM？它处在什么位置？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;大厂面试题：你不得不掌握的&#32;JVM&#32;内存管理.md">02 大厂面试题：你不得不掌握的 JVM 内存管理.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;大厂面试题：从覆盖&#32;JDK&#32;的类开始掌握类的加载机制.md">03 大厂面试题：从覆盖 JDK 的类开始掌握类的加载机制.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;动手实践：从栈帧看字节码是如何在&#32;JVM&#32;中进行流转的.md">04 动手实践：从栈帧看字节码是如何在 JVM 中进行流转的.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;大厂面试题：得心应手应对&#32;OOM&#32;的疑难杂症.md">05 大厂面试题：得心应手应对 OOM 的疑难杂症.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;深入剖析：垃圾回收你真的了解吗？（上）.md">06 深入剖析：垃圾回收你真的了解吗？（上）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;深入剖析：垃圾回收你真的了解吗？（下）.md">07 深入剖析：垃圾回收你真的了解吗？（下）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;大厂面试题：有了&#32;G1&#32;还需要其他垃圾回收器吗？.md">08 大厂面试题：有了 G1 还需要其他垃圾回收器吗？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;案例实战：亿级流量高并发下如何进行估算和调优.md">09 案例实战：亿级流量高并发下如何进行估算和调优.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;第09讲：案例实战：面对突如其来的&#32;GC&#32;问题如何下手解决.md">10 第09讲：案例实战：面对突如其来的 GC 问题如何下手解决.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;第10讲：动手实践：自己模拟&#32;JVM&#32;内存溢出场景.md">11 第10讲：动手实践：自己模拟 JVM 内存溢出场景.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;第11讲：动手实践：遇到问题不要慌，轻松搞定内存泄漏.md">12 第11讲：动手实践：遇到问题不要慌，轻松搞定内存泄漏.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;工具进阶：如何利用&#32;MAT&#32;找到问题发生的根本原因.md">13 工具进阶：如何利用 MAT 找到问题发生的根本原因.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;动手实践：让面试官刮目相看的堆外内存排查.md">14 动手实践：让面试官刮目相看的堆外内存排查.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;预警与解决：深入浅出&#32;GC&#32;监控与调优.md">15 预警与解决：深入浅出 GC 监控与调优.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;案例分析：一个高死亡率的报表系统的优化之路.md">16 案例分析：一个高死亡率的报表系统的优化之路.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;案例分析：分库分表后，我的应用崩溃了.md">17 案例分析：分库分表后，我的应用崩溃了.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;动手实践：从字节码看方法调用的底层实现.md">18 动手实践：从字节码看方法调用的底层实现.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;大厂面试题：不要搞混&#32;JMM&#32;与&#32;JVM.md">19 大厂面试题：不要搞混 JMM 与 JVM.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;动手实践：从字节码看并发编程的底层实现.md">20 动手实践：从字节码看并发编程的底层实现.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;动手实践：不为人熟知的字节码指令.md">21 动手实践：不为人熟知的字节码指令.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;深入剖析：如何使用&#32;Java&#32;Agent&#32;技术对字节码进行修改.md">22 深入剖析：如何使用 Java Agent 技术对字节码进行修改.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;动手实践：JIT&#32;参数配置如何影响程序运行？.md">23 动手实践：JIT 参数配置如何影响程序运行？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;案例分析：大型项目如何进行性能瓶颈调优？.md">24 案例分析：大型项目如何进行性能瓶颈调优？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;未来：JVM&#32;的历史与展望.md">25 未来：JVM 的历史与展望.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;福利：常见&#32;JVM&#32;面试题补充.md">26 福利：常见 JVM 面试题补充.md</a>

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
                        <div><h1>02 大厂面试题：你不得不掌握的 JVM 内存管理</h1>
<p>本课时我们主要讲解 JVM 的内存划分以及栈上的执行过程。这块内容在面试中主要涉及以下这 3 个面试题：</p>
<ul>
<li>JVM 是如何进行内存区域划分的？</li>
<li>JVM 如何高效进行内存管理？</li>
<li>为什么需要有元空间，它又涉及什么问题？</li>
</ul>
<p>带着这 3 个问题，我们开始今天的学习，关于内存划分的知识我希望在本课时你能够理解就可以，不需要死记硬背，因为在后面的课时我们会经常使用到本课时学习的内容，也会结合工作中的场景具体问题具体分析，这样你可以对 JVM 的内存获得更深刻的认识。
首先，第一个问题：**JVM的内存区域是怎么高效划分的？**这也是一个高频的面试题。很多同学可能通过死记硬背的方式来应对这个问题，这样不仅对知识没有融会贯通在面试中还很容易忘记答案。
为什么要问到 JVM 的内存区域划分呢？因为 Java 引以为豪的就是它的自动内存管理机制。相比于 C++的手动内存管理、复杂难以理解的指针等，Java 程序写起来就方便的多。
然而这种呼之即来挥之即去的内存申请和释放方式，自然也有它的代价。为了管理这些快速的内存申请释放操作，就必须引入一个池子来延迟这些内存区域的回收操作。
我们常说的内存回收，就是针对这个池子的操作。我们把上面说的这个池子，叫作堆，可以暂时把它看成一个整体。</p>
<h2></h2>
<h3><strong>JVM 内存布局</strong></h3>
<p>程序想要运行，就需要数据。有了数据，就需要在内存上存储。那你可以回想一下，我们的 C++ 程序是怎么运行的？是不是也是这样？
Java 程序的数据结构是非常丰富的。其中的内容，举一些例子：</p>
<ul>
<li>静态成员变量</li>
<li>动态成员变量</li>
<li>区域变量</li>
<li>短小紧凑的对象声明</li>
<li>庞大复杂的内存申请</li>
</ul>
<p>这么多不同的数据结构，到底是在什么地方存储的，它们之间又是怎么进行交互的呢？是不是经常在面试的时候被问到这些问题？
我们先看一下 JVM 的内存布局。随着 Java 的发展，内存布局一直在调整之中。比如，Java 8 及之后的版本，彻底移除了持久代，而使用 Metaspace 来进行替代。这也表示着 -XX:PermSize 和 -XX:MaxPermSize 等参数调优，已经没有了意义。但大体上，比较重要的内存区域是固定的。</p>
<p><img src="assets/Cgq2xl4VrjWAPqAuAARqnz6cigo666.png" alt="img" /></p>
<p>JVM 内存区域划分如图所示，从图中我们可以看出：</p>
<ul>
<li>JVM 堆中的数据是共享的，是占用内存最大的一块区域。</li>
<li>可以执行字节码的模块叫作执行引擎。</li>
<li>执行引擎在线程切换时怎么恢复？依靠的就是程序计数器。</li>
<li>JVM 的内存划分与多线程是息息相关的。像我们程序中运行时用到的栈，以及本地方法栈，它们的维度都是线程。</li>
<li>本地内存包含元数据区和一些直接内存。</li>
</ul>
<p>一般情况下，只要你能答出上面这些主要的区域，面试官都会满意的点头。但如果深挖下去，可能就有同学就比较头疼了。下面我们就详细看下这个过程。</p>
<h2></h2>
<h3><strong>虚拟机栈</strong></h3>
<p><img src="assets/CgpOIF4VrjWAejcvABlLC2rtYrw357.gif" alt="img" /></p>
<p>栈是什么样的数据结构？你可以想象一下子弹上膛的这个过程，后进的子弹最先射出，最上面的子弹就相当于栈顶。
我们在上面提到，Java 虚拟机栈是基于线程的。哪怕你只有一个 main() 方法，也是以线程的方式运行的。在线程的生命周期中，参与计算的数据会频繁地入栈和出栈，栈的生命周期是和线程一样的。
栈里的每条数据，就是栈帧。在每个 Java 方法被调用的时候，都会创建一个栈帧，并入栈。一旦完成相应的调用，则出栈。所有的栈帧都出栈后，线程也就结束了。每个栈帧，都包含四个区域：</p>
<ul>
<li>局部变量表</li>
<li>操作数栈</li>
<li>动态连接</li>
<li>返回地址</li>
</ul>
<p>我们的应用程序，就是在不断操作这些内存空间中完成的。</p>
<p><img src="assets/Cgq2xl4VrjWABK2qAATDn4DQbvE629.png" alt="img" /></p>
<p>本地方法栈是和虚拟机栈非常相似的一个区域，它服务的对象是 native 方法。你甚至可以认为虚拟机栈和本地方法栈是同一个区域，这并不影响我们对 JVM 的了解。
这里有一个比较特殊的数据类型叫作 returnAdress。因为这种类型只存在于字节码层面，所以我们平常打交道的比较少。对于 JVM 来说，程序就是存储在方法区的字节码指令，而 returnAddress 类型的值就是指向特定指令内存地址的指针。</p>
<p><img src="assets/CgpOIF4VrjWAZvMCAAB9Uu8GKww546.png" alt="img" /><br />
这部分有两个比较有意思的内容，面试中说出来会让面试官眼前一亮。</p>
<ul>
<li>这里有一个两层的栈。第一层是栈帧，对应着方法；第二层是方法的执行，对应着操作数。注意千万不要搞混了。</li>
<li>你可以看到，所有的字节码指令，其实都会抽象成对栈的入栈出栈操作。执行引擎只需要傻瓜式的按顺序执行，就可以保证它的正确性。</li>
</ul>
<p>这一点很神奇，也是基础。我们接下来从线程角度看一下里面的内容。</p>
<h2></h2>
<h3><strong>程序计数器</strong></h3>
<p>那么你设想一下，如果我们的程序在线程之间进行切换，凭什么能够知道这个线程已经执行到什么地方呢？
既然是线程，就代表它在获取 CPU 时间片上，是不可预知的，需要有一个地方，对线程正在运行的点位进行缓冲记录，以便在获取 CPU 时间片时能够快速恢复。
就好比你停下手中的工作，倒了杯茶，然后如何继续之前的工作？
程序计数器是一块较小的内存空间，它的作用可以看作是当前线程所执行的字节码的行号指示器。这里面存的，就是当前线程执行的进度。下面这张图，能够加深大家对这个过程的理解。</p>
<p><img src="assets/Cgq2xl4VrjaANruFAAQKxZvgfSs652.png" alt="img" /></p>
<p>可以看到，程序计数器也是因为线程而产生的，与虚拟机栈配合完成计算操作。程序计数器还存储了当前正在运行的流程，包括正在执行的指令、跳转、分支、循环、异常处理等。
我们可以看一下程序计数器里面的具体内容。下面这张图，就是使用 javap 命令输出的字节码。大家可以看到在每个 opcode 前面，都有一个序号。就是图中红框中的偏移地址，你可以认为它们是程序计数器的内容。</p>
<p><img src="assets/CgpOIF4VrjaAQSVlAAB8U3OQQR8670.jpg" alt="img" /></p>
<h2></h2>
<h3><strong>堆</strong></h3>
<p><img src="assets/Cgq2xl4VrjaAXnuQAANJIXDvNhI844.png" alt="img" /></p>
<p>堆是 JVM 上最大的内存区域，我们申请的几乎所有的对象，都是在这里存储的。我们常说的垃圾回收，操作的对象就是堆。
堆空间一般是程序启动时，就申请了，但是并不一定会全部使用。
随着对象的频繁创建，堆空间占用的越来越多，就需要不定期的对不再使用的对象进行回收。这个在 Java 中，就叫作 GC（Garbage Collection）。
由于对象的大小不一，在长时间运行后，堆空间会被许多细小的碎片占满，造成空间浪费。所以，仅仅销毁对象是不够的，还需要堆空间整理。这个过程非常的复杂，我们会在后面有专门的课时进行介绍。
那一个对象创建的时候，到底是在堆上分配，还是在栈上分配呢？这和两个方面有关：对象的类型和在 Java 类中存在的位置。
Java 的对象可以分为基本数据类型和普通对象。
对于普通对象来说，JVM 会首先在堆上创建对象，然后在其他地方使用的其实是它的引用。比如，把这个引用保存在虚拟机栈的局部变量表中。
对于基本数据类型来说（byte、short、int、long、float、double、char)，有两种情况。
我们上面提到，每个线程拥有一个虚拟机栈。当你在方法体内声明了基本数据类型的对象，它就会在栈上直接分配。其他情况，都是在堆上分配。
注意，像 int[] 数组这样的内容，是在堆上分配的。数组并不是基本数据类型。</p>
<p>这就是 JVM 的基本的内存分配策略。而堆是所有线程共享的，如果是多个线程访问，会涉及数据同步问题。这同样是个大话题，我们在这里先留下一个悬念。</p>
<h2></h2>
<h3><strong>元空间</strong></h3>
<p>关于元空间，我们还是以一个非常高频的面试题开始：“为什么有 Metaspace 区域？它有什么问题？”
说到这里，你应该回想一下类与对象的区别。对象是一个活生生的个体，可以参与到程序的运行中；类更像是一个模版，定义了一系列属性和操作。那么你可以设想一下。我们前面生成的 A.class，是放在 JVM 的哪个区域的？
想要问答这个问题，就不得不提下 Java 的历史。在 Java 8 之前，这些类的信息是放在一个叫 Perm 区的内存里面的。更早版本，甚至 String.intern 相关的运行时常量池也放在这里。这个区域有大小限制，很容易造成 JVM 内存溢出，从而造成 JVM 崩溃。
Perm 区在 Java 8 中已经被彻底废除，取而代之的是 Metaspace。原来的 Perm 区是在堆上的，现在的元空间是在非堆上的，这是背景。关于它们的对比，可以看下这张图。</p>
<p><img src="assets/Cgq2xl4VrjaAIlgaAAJKReuKXII670.png" alt="img" /></p>
<p>然后，元空间的好处也是它的坏处。使用非堆可以使用操作系统的内存，JVM 不会再出现方法区的内存溢出；但是，无限制的使用会造成操作系统的死亡。所以，一般也会使用参数 -XX:MaxMetaspaceSize 来控制大小。
方法区，作为一个概念，依然存在。它的物理存储的容器，就是 Metaspace。我们将在后面的课时中，再次遇到它。现在，你只需要了解到，这个区域存储的内容，包括：类的信息、常量池、方法数据、方法代码就可以了。</p>
<h2></h2>
<h3><strong>小结</strong></h3>
<p>好了，到这里本课时的基本内容就讲完了，针对这块的内容在面试中还经常会遇到下面这两个问题。</p>
<ul>
<li>我们常说的字符串常量，存放在哪呢？</li>
</ul>
<p>由于常量池，在 Java 7 之后，放到了堆中，我们创建的字符串，将会在堆上分配。</p>
<ul>
<li>堆、非堆、本地内存，有什么关系？</li>
</ul>
<p>关于它们的关系，我们可以看一张图。在我的感觉里，堆是软绵绵的，松散而有弹性；而非堆是冰冷生硬的，内存非常紧凑。</p>
<p><img src="assets/CgpOIF4VrjaAOSx2AAJgrvself8711.png" alt="img" /></p>
<p>大家都知道，JVM 在运行时，会从操作系统申请大块的堆内内存，进行数据的存储。但是，堆外内存也就是申请后操作系统剩余的内存，也会有部分受到 JVM 的控制。比较典型的就是一些 native 关键词修饰的方法，以及对内存的申请和处理。
在 Linux 机器上，使用 top 或者 ps 命令，在大多数情况下，能够看到 RSS 段（实际的内存占用），是大于给 JVM 分配的堆内存的。
如果你申请了一台系统内存为 2GB 的主机，可能 JVM 能用的就只有 1GB，这便是一个限制。</p>
<h2></h2>
<h3>总结</h3>
<p>JVM 的运行时区域是栈，而存储区域是堆。很多变量，其实在编译期就已经固定了。.class 文件的字节码，由于助记符的作用，理解起来并不是那么吃力，我们将在课程最后几个课时，从字节码层面看一下多线程的特性。
JVM 的运行时特性，以及字节码，是比较偏底层的知识。本课时属于初步介绍，有些部分并未深入讲解。希望你应该能够在脑海里建立一个 Java 程序怎么运行的概念，以便我们在后面的课时中，提到相应的内存区域时，有个整体的印象。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;一探究竟：为什么需要&#32;JVM？它处在什么位置？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;大厂面试题：从覆盖&#32;JDK&#32;的类开始掌握类的加载机制.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43587b9e09645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BA%20Java%20%E8%99%9A%E6%8B%9F%E6%9C%BA-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
