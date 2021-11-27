<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11 JDWP 简介：十步杀一人，千里不留行.md</title>
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

                    <a class="current-tab" href="11&#32;JDWP&#32;简介：十步杀一人，千里不留行.md">11 JDWP 简介：十步杀一人，千里不留行.md</a>
                    

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

                    
                    <a href="16&#32;Oracle&#32;GraalVM&#32;介绍：会当凌绝顶、一览众山小.md">16 Oracle GraalVM 介绍：会当凌绝顶、一览众山小.md</a>

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
                        <div><h1>11 JDWP 简介：十步杀一人，千里不留行</h1>
<p>Java 平台调试体系（Java Platform Debugger Architecture，JPDA），由三个相对独立的层次共同组成。这三个层次由低到高分别是 Java 虚拟机工具接口（JVMTI）、Java 调试连接协议（JDWP）以及 Java 调试接口（JDI）。</p>
<table>
<thead>
<tr>
<th align="left">模块</th>
<th align="left">层次</th>
<th align="left">编程语言</th>
<th align="left">作用</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JVMTI</td>
<td align="left">底层</td>
<td align="left">C</td>
<td align="left">获取及控制当前虚拟机状态</td>
</tr>
<tr>
<td align="left">JDWP</td>
<td align="left">中间层</td>
<td align="left">C</td>
<td align="left">定义 JVMTI 和 JDI 交互的数据格式</td>
</tr>
<tr>
<td align="left">JDI</td>
<td align="left">高层</td>
<td align="left">Java</td>
<td align="left">提供 Java API 来远程控制被调试虚拟机</td>
</tr>
</tbody>
</table>
<blockquote>
<p>详细介绍请参考或搜索：<a href="https://www.ibm.com/developerworks/cn/java/j-lo-jpda1/index.html">JPDA 体系概览</a>。</p>
</blockquote>
<h2>服务端 JVM 配置</h2>
<p>本篇主要讲解如何在 JVM 中启用 JDWP，以供远程调试。 假设主启动类是 com.xxx.Test。</p>
<p>在 Windows 机器上：</p>
<pre><code>java -Xdebug -Xrunjdwp:transport=dt_shmem,address=debug,server=y,suspend=y com.xxx.Test

</code></pre>
<p>在 Solaris 或 Linux 操作系统上：</p>
<pre><code>java -Xdebug -Xrunjdwp:transport=dt_socket,address=8888,server=y,suspend=y com.xxx.Test

</code></pre>
<p>其实，<code>-Xdebug</code> 这个选项什么用都没有，官方说是为了历史兼容性，避免报错才没有删除。</p>
<p>另外这个参数配置里的 <code>suspend=y</code> 会让 Java 进程启动时先挂起，等到有调试器连接上以后继续执行程序。</p>
<p>而如果改成 <code>suspend=n</code> 的话，则此 Java 进程会直接执行，但是我们可以随时通过调试器连上进程。</p>
<p>就是说，比如说我们启动一个 Web 服务器进程，当这个值是 y 的时候，服务器的 JVM 初始化以后不会启动 Web 服务器，会一直等到我们用 IDEA 或 Eclipse、JDB 等工具连上这个 Java 进程后，再继续启动 Web 服务器。而如果是 n 的话，则会不管有没有调试器连接，都会正常运行。</p>
<p>通过这些启动参数，Test 类将运行在调试模式下，并等待调试器连接到 JVM 的调试地址：在 Windows 上是 Debug，在 Oracle Solaris 或 Linux 操作系统上是 8888 端口。</p>
<blockquote>
<p>如果细心观察的话，会发现 IDEA 中 Debug 模式启动的程序，自动设置了类似的启动选项。</p>
</blockquote>
<h2>JDB</h2>
<p>启用了 JDWP 之后，可以使用各种客户端来进行调试/远程调试。比如 JDB 调试本地 JVM：</p>
<pre><code>jdb -attach 'debug'
jdb -attach 8888

</code></pre>
<p>当 JDB 初始化并连接到 Test 之后，就可以进行 Java 代码级（Java-level）的调试。</p>
<p>但是 JDB 调试非常麻烦，比如说几个常用命令：</p>
<p>\1. 设置断点：</p>
<pre><code>stop at 类名:行号 

</code></pre>
<p>\2. 清除断点：</p>
<pre><code>clear at 类名:行号 

</code></pre>
<p>\3. 显示局部变量：</p>
<pre><code>localx

</code></pre>
<p>\4. 显示变量 a 的值：</p>
<pre><code>print a

</code></pre>
<p>\5. 显示当前线程堆栈：</p>
<pre><code>wherei

</code></pre>
<p>\6. 代码执行到下一行：</p>
<pre><code>next

</code></pre>
<p>\7. 代码继续执行，直到遇到下一个断点：</p>
<pre><code>cont

</code></pre>
<p>可以看到使用 JDB 调试的话非常麻烦，所以我们一般还是在开发工具 IDE（IDEA、Eclipse）里调试代码。</p>
<h2>开发工具 IDEA 中使用远程调试</h2>
<p>下面介绍 IDEA 中怎样使用远程调试。与常规的 Debug 配置类似，进入编辑：</p>
<p><img src="assets/5adef100-2c99-11ea-8c87-e5afec28626d" alt="749ef972-a71a-475a-a395-ab8e78db5fdf.png" /></p>
<p>添加 Remote（不是 Tomcat 下面的那个 Remote Server）：</p>
<p><img src="assets/6d83bcf0-2c99-11ea-8c87-e5afec28626d" alt="f6a45f68-6c1c-4c55-90ae-eae35c2dafc3.png" /></p>
<p>然后配置端口号，比如 8888。</p>
<p><img src="assets/7e457100-2c99-11ea-b3f5-45352c445237" alt="82bb5db4-9dc4-443d-9bb9-00864167c52f.png" /></p>
<p>然后点击应用（Apply）按钮。</p>
<p>点击 Debug 的那个按钮即可启动远程调试，连上之后就和调试本地程序一样了。当然，记得加断点或者条件断点。</p>
<p><strong>注意</strong>：远程调试时，需要保证服务端 JVM 中运行的代码和本地完全一致，否则可能会有莫名其妙的问题。</p>
<p>细心的同学可能已经发现，IDEA 给出了远程 JVM 的启动参数，建议使用 agentlib 的方式：</p>
<pre><code>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8888

</code></pre>
<p>远程调试代码不仅在开发程序的过程中非常有用，而且实际生产环境，有时候我们无法判断程序运行的过程中出现了什么问题，到时运行结果跟期望值不一致，这时候就可以使用远程调试功能连接到生产环境，从而可以追踪导致执行过程中的哪个步骤出了问题。</p>
<p>JVM 为什么可以让不同的开发工具和调试器都连接上进行调试呢？因为它提供了一套公开的调试信息的交互协议，各家厂商就可以根据这个协议去实现自己的调试图形工具，进而方便 Java 开发人员的使用。下面就简单谈谈这个协议。</p>
<h2>JDWP 协议规范</h2>
<p>JDWP 全称是 Java Debug Wire Protocol，中文翻译为“Java 调试连接协议”，是用于规范调试器（Debugger）与目标 JVM 之间通信的协议。</p>
<p>JDWP 是一个可选组件，可能在某些 JDK 实现中不可用。</p>
<p>JDWP 支持两种调试场景：</p>
<ul>
<li>同一台计算机上的其他进程</li>
<li>远程计算机上</li>
</ul>
<p>与许多协议规范的不同之处在于，JDWP 只规定了具体的格式和布局，而不管你用什么协议来传输数据。</p>
<p>JDWP 实现可以只使用简单的 API 来接受不同的传输机制。具体的传输不一定支持各种组合。</p>
<p>JDWP 设计得非常简洁，容易实现，而且对于未来的升级也足够灵活。</p>
<p>当前，JDWP 没有指定任何传输机制。将来如果发生变更，会在单独的文档中来进行规范。</p>
<p>JDWP 是 JPDA 中的一层。JPDA（Java Platform Debugger Architecture，Java 平台调试器体系结构）架构还包含更上层的 Java 调试接口（JDI，Java Debug Interface）。JDWP 旨在促进 JDI 的有效使用；为此，它的许多功能都是量身定制的。</p>
<p>对于那些用 Java 语言编写的 Debugger 工具来说，直接使用 JDI 比起 JDWP 更加方便。</p>
<p>有关 JPDA 的更多信息，请参考：</p>
<blockquote>
<p><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/index.html">Java Platform Debugger Architecture documentation</a></p>
</blockquote>
<h2>JDWP 握手过程</h2>
<p>连接建立之后，在发送其他数据包之前，连接双方需要进行握手：</p>
<p>握手过程包括以下步骤：</p>
<ul>
<li>Debugger 端向目标 JVM 发送 14 个字节，也就是包括 14 个 ASCII 字符的字符串 &quot;JDWP-Handshake&quot;。</li>
<li>VM 端以相同的 14 个字节答复：JDWP-Handshake。</li>
</ul>
<h2>JDWP 数据包</h2>
<p>JDWP 是无状态的协议，基于数据包来传输数据。包含两种基本的数据包类型：命令包（Command Packet）和应答包（Reply Packet）。</p>
<p>调试器和目标 VM 都可以发出命令包，调试器可以用命令包来从目标 VM 请求相关信息或者控制程序的执行，目标 VM 可以将自身的某些事件（例如断点或异常）用命令数据包的方式通知调试器。</p>
<p>应答包仅用于对命令包进行响应，并且标明该命令是成功还是失败。 应答包还可以携带命令中请求的数据（例如字段或变量的值）。当前，从目标 VM 发出的事件不需要调试器的应答。</p>
<p>JDWP 是异步的，在收到某个应答之前，可以发送多个命令包。</p>
<p>命令包和应答包的 header 大小相等。这样使传输更易于实现和抽象。每个数据包的布局如下所示。</p>
<p><strong>命令包（Command Packet）</strong></p>
<ul>
<li>Header
<ul>
<li>length（4 bytes）</li>
<li>id（4 bytes）</li>
<li>flags（1 byte）</li>
<li>command set（1 byte）</li>
<li>command（1 byte）</li>
</ul>
</li>
<li>data（长度不固定）</li>
</ul>
<p><strong>应答包（Reply Packet）</strong></p>
<ul>
<li>Header
<ul>
<li>length（4 bytes）</li>
<li>id（4 bytes）</li>
<li>flags（1 byte）</li>
<li>error code（2 bytes）</li>
</ul>
</li>
<li>data（Variable）</li>
</ul>
<p>可以看到，这两种数据包的 Header 中，前三个字段格式是相同的。</p>
<p>通过 JDWP 发送的所有字段和数据都应采用大端字节序（big-endian）。大端字节序的定义请参考《Java 虚拟机规范》。</p>
<h2>数据包字段说明</h2>
<h3>通用 Header 字段</h3>
<p>下面的 Header 字段是命令包与应答包通用的。</p>
<p><strong>length</strong></p>
<p>length 字段表示整个数据包（包括 header）的字节数。因为数据包 header 的大小为 11 个字节，因此没有 data 的数据包会将此字段值设置为 11。</p>
<p><strong>id</strong></p>
<p>id 字段用于唯一标识每一对数据包（command/reply）。应答包 id 值必须与对应的命令包 ID 相同。这样异步方式的命令和应答就能匹配起来。同一个来源发送的所有未完成命令包的 id 字段必须唯一。（调试器发出的命令包，与 JVM 发出的命令包如果 ID 相同也没关系。） 除此之外，对 ID 的分配没有任何要求。对于大多数实现而言，使用自增计数器就足够了。id 的取值允许 2^32 个数据包，足以应对各种调试场景。</p>
<p><strong>flags</strong></p>
<p>flags 标志用于修改命令的排队和处理方式，也用来标记源自 JVM 的数据包。当前只定义了一个标志位 0x80，表示此数据包是应答包。协议的未来版本可能会定义其他标志。</p>
<h3>命令包的 Header</h3>
<p>除了前面的通用 Header 字段，命令包还有以下请求头。</p>
<p><strong>command set</strong></p>
<p>该字段主要用于通过一种有意义的方式对命令进行分组。Sun 定义的命令集，通过在 JDI 中支持的接口进行分组。例如，所有支持 VirtualMachine 接口的命令都在 VirtualMachine 命令集里面。命令集空间大致分为以下几类：</p>
<ul>
<li>0-63：发给目标 VM 的命令集</li>
<li>64-127：发送给调试器的命令集</li>
<li>128-256：JVM 提供商自己定义的命令和扩展。</li>
</ul>
<p><strong>command</strong></p>
<p>该字段用于标识命令集中的具体命令。该字段与命令集字段一起用于指示应如何处理命令包。更简洁地说，它们告诉接收者该怎么做。具体命令将在本文档后面介绍。</p>
<h3>应答包的 Header</h3>
<p>除了前面的通用 Header 字段，应答包还有以下请求头。</p>
<p><strong>error code</strong></p>
<p>此字段用于标识是否成功处理了对应的命令包。0 值表示成功，非零值表示错误。返回的错误代码由具体的命令集/命令规定，但是通常会映射为 JVM TI 标准错误码。</p>
<h3>Data</h3>
<p>每个命令的 Data 部分都是不同的。相应的命令包和应答包之间也有所不同。例如，请求命令包希望获取某个字段的值，可以在 Data 中填上 object ID 和 field ID。应答包的 Data 字段将存放该字段的值。</p>
<h2>JDWP 中常用的数据类型</h2>
<p>通常，命令或应答包的 Data 字段格式由具体的命令规定。Data 中的每个字段都是（Java 标准的）大端格式编码。下面介绍每个 Data 字段的数据类型。</p>
<p>大部分 JDWP 数据包中的数据类型如下所述。</p>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Size</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">byte</td>
<td align="left">1 byte</td>
</tr>
<tr>
<td align="left">boolean</td>
<td align="left">1 byte</td>
</tr>
<tr>
<td align="left">int</td>
<td align="left">4 bytes</td>
</tr>
<tr>
<td align="left">long</td>
<td align="left">8 bytes</td>
</tr>
<tr>
<td align="left">objectID</td>
<td align="left">由具体的 JVM 确定，最多 8 字节</td>
</tr>
<tr>
<td align="left">tagged-objectID</td>
<td align="left">objectID 的大小 +1 字节</td>
</tr>
<tr>
<td align="left">threadID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">threadGroupID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">stringID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">classLoaderID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">classObjectID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">arrayID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">referenceTypeID</td>
<td align="left">同 objectID</td>
</tr>
<tr>
<td align="left">classID</td>
<td align="left">同 referenceTypeID</td>
</tr>
<tr>
<td align="left">interfaceID</td>
<td align="left">同 referenceTypeID</td>
</tr>
<tr>
<td align="left">arrayTypeID</td>
<td align="left">同 referenceTypeID</td>
</tr>
<tr>
<td align="left">methodID</td>
<td align="left">由具体的 JVM 确定，最多 8 字节</td>
</tr>
<tr>
<td align="left">fieldID</td>
<td align="left">由具体的 JVM 确定，最多 8 字节</td>
</tr>
<tr>
<td align="left">frameID</td>
<td align="left">由具体的 JVM 确定，最多 8 字节</td>
</tr>
<tr>
<td align="left">location</td>
<td align="left">由具体的 JVM 确定</td>
</tr>
<tr>
<td align="left">string</td>
<td align="left">长度不固定</td>
</tr>
<tr>
<td align="left">value</td>
<td align="left">长度不固定</td>
</tr>
<tr>
<td align="left">untagged-value</td>
<td align="left">长度不固定</td>
</tr>
<tr>
<td align="left">arrayregion</td>
<td align="left">长度不固定</td>
</tr>
</tbody>
</table>
<p>不同的 JVM 中，Object IDs、Reference Type IDs、Field IDs、Method IDs 和 Frame IDs 的大小可能不同。</p>
<p>通常，它们的大小与 JNI 和 JVMDI 调用中用于这些项目的 native 标识符的大小相对应。这些类型中最大的 size 为 8 个字节。当然，调试器可以使用 &quot;idSizes&quot; 这个命令来确定每种类型的大小。</p>
<p>如果 JVM 收到的命令包里面含有未实现（non-implemented）或无法识别（non-recognized）的命令/命令集，则会返回带有错误码 NOT_IMPLEMENTED 的应答包。具体的错误常量可参考：</p>
<blockquote>
<p><a href="https://docs.oracle.com/javase/8/docs/platform/jpda/jdwp/jdwp-protocol.html#JDWP_Error">Error Constants</a></p>
</blockquote>
<h2>参考文档</h2>
<ul>
<li><a href="https://docs.oracle.com/javase/8/docs/platform/jpda/jdwp/jdwp-protocol.html">JDWP 协议的具体命令</a></li>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/index.html">Java Platform Debugger Architecture</a></li>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/jdwp-spec.html">JDWP Specification</a></li>
<li><a href="https://www.jianshu.com/p/5a64ed722b91">使用 JDB 进行调试</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;JDK&#32;内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;JMX&#32;与相关工具：山高月小，水落石出.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340c53e7c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
