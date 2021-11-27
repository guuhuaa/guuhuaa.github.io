<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09 JDK 内置命令行工具：工欲善其事，必先利其器.md</title>
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

                    <a class="current-tab" href="09&#32;JDK&#32;内置命令行工具：工欲善其事，必先利其器.md">09 JDK 内置命令行工具：工欲善其事，必先利其器.md</a>
                    

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
                        <div><h1>09 JDK 内置命令行工具：工欲善其事，必先利其器</h1>
<p>很多情况下，JVM 运行环境中并没有趁手的工具，所以掌握基本的内置工具是一项基本功。</p>
<p>JDK 自带的工具和程序可以分为 2 大类型：</p>
<ol>
<li>开发工具</li>
<li>诊断分析工具</li>
</ol>
<h3>JDK 内置的开发工具</h3>
<p>写过 Java 程序的同学，对 JDK 中的开发工具应该比较熟悉。 下面列举常用的部分：</p>
<table>
<thead>
<tr>
<th align="left">工具</th>
<th align="left">简介</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">java</td>
<td align="left">Java 应用的启动程序</td>
</tr>
<tr>
<td align="left">javac</td>
<td align="left">JDK 内置的编译工具</td>
</tr>
<tr>
<td align="left">javap</td>
<td align="left">反编译 class 文件的工具</td>
</tr>
<tr>
<td align="left"><strong>javadoc</strong></td>
<td align="left">根据 Java 代码和标准注释，自动生成相关的 API 说明文档</td>
</tr>
<tr>
<td align="left"><strong>javah</strong></td>
<td align="left">JNI 开发时，根据 Java 代码生成需要的 .h 文件。</td>
</tr>
<tr>
<td align="left">extcheck</td>
<td align="left">检查某个 jar 文件和运行时扩展 jar 有没有版本冲突，很少使用</td>
</tr>
<tr>
<td align="left">jdb</td>
<td align="left">Java Debugger 可以调试本地和远端程序，属于 JPDA 中的一个 Demo 实现，供其他调试器参考。开发时很少使用</td>
</tr>
<tr>
<td align="left">jdeps</td>
<td align="left">探测 class 或 jar 包需要的依赖</td>
</tr>
<tr>
<td align="left">jar</td>
<td align="left">打包工具，可以将文件和目录打包成为 .jar 文件；.jar 文件本质上就是 zip 文件，只是后缀不同。使用时按顺序对应好选项和参数即可。</td>
</tr>
<tr>
<td align="left">keytool</td>
<td align="left">安全证书和密钥的管理工具（支持生成、导入、导出等操作）</td>
</tr>
<tr>
<td align="left">jarsigner</td>
<td align="left">jar 文件签名和验证工具</td>
</tr>
<tr>
<td align="left">policytool</td>
<td align="left">实际上这是一款图形界面工具，管理本机的 Java 安全策略</td>
</tr>
</tbody>
</table>
<p>开发工具此处不做详细介绍，有兴趣的同学请参考文末的链接。</p>
<p>下面介绍诊断和分析工具。</p>
<h3>命令行诊断和分析工具</h3>
<p>JDK 内置了各种命令行工具，条件受限时我们可以先用命令行工具快速查看 JVM 实例的基本情况。</p>
<blockquote>
<p>macOS X、Windows 系统的某些账户权限不够，有些工具可能会报错/失败，假如出问题了请排除这个因素。</p>
</blockquote>
<h3>JPS 工具简介</h3>
<p>我们知道，操作系统提供一个工具叫做 ps，用于显示进程状态（Process Status）。</p>
<p>Java也 提供了类似的命令行工具，叫做 JPS，用于展示 Java 进程信息（列表）。</p>
<p>需要注意的是，JPS 展示的是当前用户可看见的 Java 进程，如果看不见某些进程可能需要 sudo、su 之类的命令来切换权限。</p>
<p>查看帮助信息：</p>
<blockquote>
<p>$ <code>jps -help</code></p>
</blockquote>
<pre><code class="language-shell">usage: jps [-help]
       jps [-q] [-mlvV] [&lt;hostid&gt;]
Definitions:
    &lt;hostid&gt;:      &lt;hostname&gt;[:&lt;port&gt;]

</code></pre>
<p>可以看到， 这些参数分为了多个组，<code>-help</code>、<code>-q</code>、<code>-mlvV</code>， 同一组可以共用一个 <code>-</code>。</p>
<p>常用参数是小写的 <code>-v</code>，显示传递给 JVM 的启动参数。</p>
<blockquote>
<p>$ <code>jps -v</code></p>
</blockquote>
<pre><code>15883 Jps -Dapplication.home=/usr/local/jdk1.8.0_74 -Xms8m
6446 Jstatd -Dapplication.home=/usr/local/jdk1.8.0_74 -Xms8m
        -Djava.security.policy=/etc/java/jstatd.all.policy
32383 Bootstrap -Xmx4096m -XX:+UseG1GC -verbose:gc
        -XX:+PrintGCDateStamps -XX:+PrintGCDetails
        -Xloggc:/xxx-tomcat/logs/gc.log
        -Dcatalina.base=/xxx-tomcat -Dcatalina.home=/data/tomcat

</code></pre>
<p>看看输出的内容，其中最重要的信息是前面的进程 ID（PID）。</p>
<p>其他参数不太常用：</p>
<ul>
<li><code>-q</code>：只显示进程号。</li>
<li><code>-m</code>：显示传给 main 方法的参数信息</li>
<li><code>-l</code>：显示启动 class 的完整类名，或者启动 jar 的完整路径</li>
<li><code>-V</code>：大写的 V，这个参数有问题，相当于没传一样。官方说的跟 <code>-q</code> 差不多。</li>
<li><code>&lt;hostid&gt;</code>：部分是远程主机的标识符，需要远程主机启动 <code>jstatd</code> 服务器支持。</li>
</ul>
<p>可以看到，格式为 <code>&lt;hostname&gt;[:&lt;port&gt;]</code>，不能用 IP，示例：<code>jps -v sample.com:1099</code>。</p>
<p>知道 JVM 进程的 PID 之后，就可以使用其他工具来进行诊断了。</p>
<h3>jstat 工具简介</h3>
<p>jstat 用来监控 JVM 内置的各种统计信息，主要是内存和 GC 相关的信息。</p>
<p>查看 jstat 的帮助信息，大致如下：</p>
<blockquote>
<p>$ <code>jstat -help</code></p>
</blockquote>
<pre><code>Usage: jstat -help|-options
       jstat -&lt;option&gt; [-t] [-h&lt;lines&gt;] &lt;vmid&gt; [&lt;interval&gt; [&lt;count&gt;]]

Definitions:
  &lt;option&gt;      可用的选项，查看详情请使用 -options
  &lt;vmid&gt;        虚拟机标识符，格式：&lt;lvmid&gt;[@&lt;hostname&gt;[:&lt;port&gt;]]
  &lt;lines&gt;       标题行间隔的频率.
  &lt;interval&gt;    采样周期，&lt;n&gt;[&quot;ms&quot;|&quot;s&quot;]，默认单位是毫秒 &quot;ms&quot;
  &lt;count&gt;       采用总次数
  -J&lt;flag&gt;      传给jstat底层JVM的 &lt;flag&gt; 参数

</code></pre>
<p>再来看看 <code>&lt;option&gt;</code> 部分支持哪些选项：</p>
<blockquote>
<p>$ <code>jstat -options</code></p>
</blockquote>
<pre><code>-class
-compiler
-gc
-gccapacity
-gccause
-gcmetacapacity
-gcnew
-gcnewcapacity
-gcold
-gcoldcapacity
-gcutil
-printcompilation

</code></pre>
<p>简单说明这些选项，不感兴趣可以跳着读。</p>
<ul>
<li><code>-class</code>：类加载（Class loader）信息统计。</li>
<li><code>-compiler</code>：JIT 即时编译器相关的统计信息。</li>
<li><code>-gc</code>：GC 相关的堆内存信息，用法：<code>jstat -gc -h 10 -t 864 1s 20</code>。</li>
<li><code>-gccapacity</code>：各个内存池分代空间的容量。</li>
<li><code>-gccause</code>：看上次 GC、本次 GC（如果正在 GC 中）的原因，其他输出和 <code>-gcutil</code> 选项一致。</li>
<li><code>-gcnew</code>：年轻代的统计信息（New = Young = Eden + S0 + S1）。</li>
<li><code>-gcnewcapacity</code>：年轻代空间大小统计。</li>
<li><code>-gcold</code>：老年代和元数据区的行为统计。</li>
<li><code>-gcoldcapacity</code>：old 空间大小统计。</li>
<li><code>-gcmetacapacity</code>：meta 区大小统计。</li>
<li><code>-gcutil</code>：GC 相关区域的使用率（utilization）统计。</li>
<li><code>-printcompilation</code>：打印 JVM 编译统计信息。</li>
</ul>
<p>实例：</p>
<pre><code class="language-shell">jstat -gcutil -t 864

</code></pre>
<p><code>-gcutil</code> 选项是统计 GC 相关区域的使用率（utilization），结果如下：</p>
<table>
<thead>
<tr>
<th align="left">Timestamp</th>
<th align="left">S0</th>
<th align="left">S1</th>
<th align="left">E</th>
<th align="left">O</th>
<th align="left">M</th>
<th align="left">CCS</th>
<th align="left">YGC</th>
<th align="left">YGCT</th>
<th align="left">FGC</th>
<th align="left">FGCT</th>
<th align="left">GCT</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">14251645.5</td>
<td align="left">0.00</td>
<td align="left">13.50</td>
<td align="left">55.05</td>
<td align="left">71.91</td>
<td align="left">83.84</td>
<td align="left">69.52</td>
<td align="left">113767</td>
<td align="left">206.036</td>
<td align="left">4</td>
<td align="left">0.122</td>
<td align="left">206.158</td>
</tr>
</tbody>
</table>
<p><code>-t</code> 选项的位置是固定的，不能在前也不能在后。可以看出是用于显示时间戳，即 JVM 启动到现在的秒数。</p>
<p>简单分析一下：</p>
<ul>
<li>Timestamp 列：JVM 启动了 1425 万秒，大约 164 天。</li>
<li>S0：就是 0 号存活区的百分比使用率。0% 很正常，因为 S0 和 S1 随时有一个是空的。</li>
<li>S1：就是 1 号存活区的百分比使用率。</li>
<li>E：就是 Eden 区，新生代的百分比使用率。</li>
<li>O：就是 Old 区，老年代。百分比使用率。</li>
<li>M：就是 Meta 区，元数据区百分比使用率。</li>
<li>CCS：压缩 class 空间（Compressed class space）的百分比使用率。</li>
<li>YGC（Young GC）：年轻代 GC 的次数。11 万多次，不算少。</li>
<li>YGCT 年轻代 GC 消耗的总时间。206 秒，占总运行时间的万分之一不到，基本上可忽略。</li>
<li>FGC：FullGC 的次数，可以看到只发生了 4 次，问题应该不大。</li>
<li>FGCT：FullGC 的总时间，0.122 秒，平均每次 30ms 左右，大部分系统应该能承受。</li>
<li>GCT：所有 GC 加起来消耗的总时间，即 YGCT + FGCT。</li>
</ul>
<p>可以看到，<code>-gcutil</code> 这个选项出来的信息不太好用，统计的结果是百分比，不太直观。</p>
<p>再看看 <code>-gc</code> 选项，GC 相关的堆内存信息。</p>
<pre><code class="language-shell">jstat -gc -t 864 1s
jstat -gc -t 864 1s 3
jstat -gc -t -h 10 864 1s 15

</code></pre>
<p>其中的 <code>1s</code> 占了 <code>&lt;interval&gt;</code> 这个槽位，表示每 1 秒输出一次信息。</p>
<p><code>1s 3</code> 的意思是每秒输出 1 次，最多 3 次。</p>
<p>如果只指定刷新周期，不指定 <code>&lt;count&gt;</code> 部分，则会一直持续输出。 退出输出按 <code>CTRL+C</code> 即可。</p>
<p><code>-h 10</code> 的意思是每 10 行输出一次表头。</p>
<p>结果大致如下：</p>
<table>
<thead>
<tr>
<th align="left">Timestamp</th>
<th align="left">S0C</th>
<th align="left">S1C</th>
<th align="left">S0U</th>
<th align="left">S1U</th>
<th align="left">EC</th>
<th align="left">EU</th>
<th align="left">OC</th>
<th align="left">OU</th>
<th align="left">MC</th>
<th align="left">MU</th>
<th align="left">YGC</th>
<th align="left">YGCT</th>
<th align="left">FGC</th>
<th align="left">FGCT</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">14254245.3</td>
<td align="left">1152.0</td>
<td align="left">1152.0</td>
<td align="left">145.6</td>
<td align="left">0.0</td>
<td align="left">9600.0</td>
<td align="left">2312.8</td>
<td align="left">11848.0</td>
<td align="left">8527.3</td>
<td align="left">31616.0</td>
<td align="left">26528.6</td>
<td align="left">113788</td>
<td align="left">206.082</td>
<td align="left">4</td>
<td align="left">0.122</td>
</tr>
<tr>
<td align="left">14254246.3</td>
<td align="left">1152.0</td>
<td align="left">1152.0</td>
<td align="left">145.6</td>
<td align="left">0.0</td>
<td align="left">9600.0</td>
<td align="left">2313.1</td>
<td align="left">11848.0</td>
<td align="left">8527.3</td>
<td align="left">31616.0</td>
<td align="left">26528.6</td>
<td align="left">113788</td>
<td align="left">206.082</td>
<td align="left">4</td>
<td align="left">0.122</td>
</tr>
<tr>
<td align="left">14254247.3</td>
<td align="left">1152.0</td>
<td align="left">1152.0</td>
<td align="left">145.6</td>
<td align="left">0.0</td>
<td align="left">9600.0</td>
<td align="left">2313.4</td>
<td align="left">11848.0</td>
<td align="left">8527.3</td>
<td align="left">31616.0</td>
<td align="left">26528.6</td>
<td align="left">113788</td>
<td align="left">206.082</td>
<td align="left">4</td>
<td align="left">0.122</td>
</tr>
</tbody>
</table>
<p>上面的结果是精简过的，为了排版去掉了 GCT、CCSC、CCSU 这三列。看到这些单词可以试着猜一下意思，详细的解读如下：</p>
<ul>
<li>Timestamp 列：JVM 启动了 1425 万秒，大约 164 天。</li>
<li>S0C：0 号存活区的当前容量（capacity），单位 kB。</li>
<li>S1C：1 号存活区的当前容量，单位 kB。</li>
<li>S0U：0 号存活区的使用量（utilization），单位 kB。</li>
<li>S1U：1 号存活区的使用量，单位 kB。</li>
<li>EC：Eden 区，新生代的当前容量，单位 kB。</li>
<li>EU：Eden 区，新生代的使用量，单位 kB。</li>
<li>OC：Old 区，老年代的当前容量，单位 kB。</li>
<li>OU：Old 区，老年代的使用量，单位 kB。 （需要关注）</li>
<li>MC：元数据区的容量，单位 kB。</li>
<li>MU：元数据区的使用量，单位 kB。</li>
<li>CCSC：压缩的 class 空间容量，单位 kB。</li>
<li>CCSU：压缩的 class 空间使用量，单位 kB。</li>
<li>YGC：年轻代 GC 的次数。</li>
<li>YGCT：年轻代 GC 消耗的总时间。 （重点关注）</li>
<li>FGC：Full GC 的次数</li>
<li>FGCT：Full GC 消耗的时间。 （重点关注）</li>
<li>GCT：垃圾收集消耗的总时间。</li>
</ul>
<p>最重要的信息是 GC 的次数和总消耗时间，其次是老年代的使用量。</p>
<p>在没有其他监控工具的情况下， jstat 可以简单查看各个内存池和 GC 的信息，可用于判别是否是 GC 问题或者内存溢出。</p>
<h3>jmap 工具</h3>
<p>面试最常问的就是 jmap 工具了。jmap 主要用来 Dump 堆内存。当然也支持输出统计信息。</p>
<p>官方推荐使用 JDK 8 自带的 jcmd 工具来取代 jmap，但是 jmap 深入人心，jcmd 可能暂时取代不了。</p>
<p>查看 jmap 帮助信息：</p>
<blockquote>
<p>$ <code>jmap -help</code></p>
</blockquote>
<pre><code>Usage:
    jmap [option] &lt;pid&gt;
        (连接到本地进程)
    jmap [option] &lt;executable &lt;core&gt;
        (连接到 core file)
    jmap [option] [<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="cbb8aeb9bdaeb994a2af8b">[email&#160;protected]</a>]&lt;remote-IP-hostname&gt;
        (连接到远程 debug 服务)

where &lt;option&gt; is one of:
    &lt;none&gt;               等同于 Solaris 的 pmap 命令
    -heap                打印 Java 堆内存汇总信息
    -histo[:live]        打印 Java 堆内存对象的直方图统计信息
                         如果指定了 &quot;live&quot; 选项则只统计存活对象，强制触发一次 GC
    -clstats             打印 class loader 统计信息
    -finalizerinfo       打印等待 finalization 的对象信息
    -dump:&lt;dump-options&gt; 将堆内存 dump 为 hprof 二进制格式
                         支持的 dump-options：
                           live         只 dump 存活对象，不指定则导出全部。
                           format=b     二进制格式(binary format)
                           file=&lt;file&gt;  导出文件的路径
                         示例：jmap -dump:live,format=b,file=heap.bin &lt;pid&gt;
    -F                   强制导出，若 jmap 被 hang 住不响应，可断开后使用此选项。
                         其中 &quot;live&quot; 选项不支持强制导出。
    -h | -help           to print this help message
    -J&lt;flag&gt;             to pass &lt;flag&gt; directly to the runtime system

</code></pre>
<p>常用选项就 3 个：</p>
<ul>
<li><code>-heap</code>：打印堆内存（/内存池）的配置和使用信息。</li>
<li><code>-histo</code>：看哪些类占用的空间最多，直方图。</li>
<li><code>-dump:format=b,file=xxxx.hprof</code>：Dump 堆内存。</li>
</ul>
<p>示例：看堆内存统计信息。</p>
<blockquote>
<p>$ <code>jmap -heap 4524</code></p>
</blockquote>
<p>输出信息：</p>
<pre><code>Attaching to process ID 4524, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.65-b01

using thread-local object allocation.
Parallel GC with 4 thread(s)

Heap Configuration:
   MinHeapFreeRatio         = 0
   MaxHeapFreeRatio         = 100
   MaxHeapSize              = 2069889024 (1974.0MB)
   NewSize                  = 42991616 (41.0MB)
   MaxNewSize               = 689963008 (658.0MB)
   OldSize                  = 87031808 (83.0MB)
   NewRatio                 = 2
   SurvivorRatio            = 8
   MetaspaceSize            = 21807104 (20.796875MB)
   CompressedClassSpaceSize = 1073741824 (1024.0MB)
   MaxMetaspaceSize         = 17592186044415 MB
   G1HeapRegionSize         = 0 (0.0MB)

Heap Usage:
PS Young Generation
Eden Space:
   capacity = 24117248 (23.0MB)
   used     = 11005760 (10.49591064453125MB)
   free     = 13111488 (12.50408935546875MB)
   45.63439410665761% used
From Space:
   capacity = 1048576 (1.0MB)
   used     = 65536 (0.0625MB)
   free     = 983040 (0.9375MB)
   6.25% used
To Space:
   capacity = 1048576 (1.0MB)
   used     = 0 (0.0MB)
   free     = 1048576 (1.0MB)
   0.0% used
PS Old Generation
   capacity = 87031808 (83.0MB)
   used     = 22912000 (21.8505859375MB)
   free     = 64119808 (61.1494140625MB)
   26.32600715361446% used

12800 interned Strings occupying 1800664 bytes.

</code></pre>
<ul>
<li>Attached，连着；</li>
<li>Detached，分离。</li>
</ul>
<p>可以看到堆内存和内存池的相关信息。当然，这些信息有多种方式可以得到，比如 JMX。</p>
<p>看看直方图：</p>
<blockquote>
<p>$ <code>jmap -histo 4524</code></p>
</blockquote>
<p>结果为：</p>
<pre><code> num     #instances         #bytes  class name
----------------------------------------------
   1:         52214       11236072  [C
   2:        126872        5074880  java.util.TreeMap$Entry
   3:          5102        5041568  [B
   4:         17354        2310576  [I
   5:         45258        1086192  java.lang.String
......

</code></pre>
<p>简单分析，其中 <code>[C</code> 占用了 11MB 内存，没占用什么空间。</p>
<p><code>[C</code> 表示 <code>chat[]</code>，<code>[B</code> 表示 <code>byte[]</code>，<code>[I</code> 表示 <code>int[]</code>，其他类似。这种基础数据类型很难分析出什么问题。</p>
<p>Java 中的大对象、巨无霸对象，一般都是长度很大的数组。</p>
<p>Dump 堆内存：</p>
<pre><code class="language-shell">cd $CATALINA_BASE
jmap -dump:format=b,file=3826.hprof 3826

</code></pre>
<p>导出完成后，dump 文件大约和堆内存一样大。可以想办法压缩并传输。</p>
<p>分析 hprof 文件可以使用 jhat 或者 <a href="https://www.eclipse.org/mat/">mat</a> 工具。</p>
<h3>jcmd 工具</h3>
<p>诊断工具：jcmd 是 JDK 8 推出的一款本地诊断工具，只支持连接本机上同一个用户空间下的 JVM 进程。</p>
<p>查看帮助：</p>
<blockquote>
<p>$ <code>jcmd -help</code></p>
</blockquote>
<pre><code class="language-shell">Usage: jcmd &lt;pid | main class&gt; &lt;command ...|PerfCounter.print|-f file&gt;
   or: jcmd -l                                                   
   or: jcmd -h                                                   

  command 必须是指定 JVM 可用的有效 jcmd 命令。     
  可以使用 &quot;help&quot; 命令查看该 JVM 支持哪些命令。  
  如果指定 pid 部分的值为 0，则会将 commands 发送给所有可见的 Java 进程。  
  指定 main class 则用来匹配启动类。可以部分匹配。（适用同一个类启动多实例）。                       
  If no options are given, lists Java processes (same as -p).    

  PerfCounter.print 命令可以展示该进程暴露的各种计数器
  -f  从文件读取可执行命令                 
  -l  列出（list）本机上可见的 JVM 进程                    
  -h  this help                          

</code></pre>
<p>查看进程信息：</p>
<pre><code class="language-shell">jcmd
jcmd -l
jps -lm

11155 org.jetbrains.idea.maven.server.RemoteMavenServer

</code></pre>
<p>这几个命令的结果差不多。可以看到其中有一个 PID 为 11155 的进程，下面看看可以用这个 PID 做什么。</p>
<p>给这个进程发一个 help 指令：</p>
<pre><code class="language-shell">jcmd 11155 help
jcmd RemoteMavenServer help

</code></pre>
<p>pid 和 main-class 输出信息是一样的：</p>
<pre><code>11155:
The following commands are available:
VM.native_memory
ManagementAgent.stop
ManagementAgent.start_local
ManagementAgent.start
GC.rotate_log
Thread.print
GC.class_stats
GC.class_histogram
GC.heap_dump
GC.run_finalization
GC.run
VM.uptime
VM.flags
VM.system_properties
VM.command_line
VM.version
help

</code></pre>
<p>可以试试这些命令。查看 VM 相关的信息：</p>
<pre><code class="language-shell"># JVM 实例运行时间
jcmd 11155 VM.uptime
9307.052 s

#JVM 版本号
jcmd 11155 VM.version
OpenJDK 64-Bit Server VM version 25.76-b162
JDK 8.0_76

# JVM 实际生效的配置参数
jcmd 11155 VM.flags
11155:
-XX:CICompilerCount=4 -XX:InitialHeapSize=268435456
-XX:MaxHeapSize=536870912 -XX:MaxNewSize=178782208
-XX:MinHeapDeltaBytes=524288 -XX:NewSize=89128960
-XX:OldSize=179306496 -XX:+UseCompressedClassPointers
-XX:+UseCompressedOops -XX:+UseParallelGC

# 查看命令行参数
jcmd 11155 VM.command_line
VM Arguments:
jvm_args: -Xmx512m -Dfile.encoding=UTF-8
java_command: org.jetbrains.idea.maven.server.RemoteMavenServer
java_class_path (initial): ...(xxx省略)...
Launcher Type: SUN_STANDARD

# 系统属性
jcmd 11155 VM.system_properties
...
java.runtime.name=OpenJDK Runtime Environment
java.vm.version=25.76-b162
java.vm.vendor=Oracle Corporation
user.country=CN

</code></pre>
<p>GC 相关的命令，统计每个类的实例占用字节数。</p>
<blockquote>
<p>$ <code>jcmd 11155 GC.class_histogram</code></p>
</blockquote>
<pre><code> num     #instances         #bytes  class name
----------------------------------------------
   1:         11613        1420944  [C
   2:          3224         356840  java.lang.Class
   3:           797         300360  [B
   4:         11555         277320  java.lang.String
   5:          1551         193872  [I
   6:          2252         149424  [Ljava.lang.Object;

</code></pre>
<p>Dump 堆内存：</p>
<blockquote>
<p>$<code>jcmd 11155 help GC.heap_dump</code></p>
</blockquote>
<pre><code class="language-shell">Syntax : GC.heap_dump [options] &lt;filename&gt;
Arguments: filename :  Name of the dump file (STRING, no default value)
Options:  -all=true 或者 -all=false (默认)

# 两者效果差不多; jcmd 需要指定绝对路径； jmap 不能指定绝对路径
jcmd 11155 GC.heap_dump -all=true ~/11155-by-jcmd.hprof
jmap -dump:file=./11155-by-jmap.hprof 11155

</code></pre>
<p>jcmd 坑的地方在于，必须指定绝对路径，否则导出的 hprof 文件就以 JVM 所在的目录计算。（因为是发命令交给 JVM 执行的）</p>
<p>其他命令用法类似，必要时请参考官方文档。</p>
<h3>jstack 工具</h3>
<p>命令行工具、诊断工具：jstack 工具可以打印出 Java 线程的调用栈信息（Stack Trace）。一般用来查看存在哪些线程，诊断是否存在死锁等。</p>
<p>这时候就看出来给线程（池）命名的必要性了（开发不规范，整个项目都是坑），具体可参考阿里巴巴的 Java 开发规范。</p>
<p>看看帮助信息：</p>
<blockquote>
<p>$<code>jstack -help</code></p>
</blockquote>
<pre><code class="language-shell">Usage:
    jstack [-l] &lt;pid&gt;
        (to connect to running process)
    jstack -F [-m] [-l] &lt;pid&gt;
        (to connect to a hung process)
    jstack [-m] [-l] &lt;executable&gt; &lt;core&gt;
        (to connect to a core file)
    jstack [-m] [-l] [<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f98a9c8b8f9c8ba6909db9">[email&#160;protected]</a>]&lt;remote server IP or hostname&gt;
        (to connect to a remote debug server)

Options:
    -F  to force a thread dump. Use when jstack &lt;pid&gt; does not respond (process is hung)
    -m  to print both java and native frames (mixed mode)
    -l  long listing. Prints additional information about locks
    -h or -help to print this help message

</code></pre>
<p>选项说明：</p>
<ul>
<li><code>-F</code>：强制执行 Thread Dump，可在 Java 进程卡死（hung 住）时使用，此选项可能需要系统权限。</li>
<li><code>-m</code>：混合模式（mixed mode），将 Java 帧和 native 帧一起输出，此选项可能需要系统权限。</li>
<li><code>-l</code>：长列表模式，将线程相关的 locks 信息一起输出，比如持有的锁，等待的锁。</li>
</ul>
<p>常用的选项是 <code>-l</code>，示例用法。</p>
<pre><code class="language-shell">jstack 4524
jstack -l 4524

</code></pre>
<p>死锁的原因一般是锁定多个资源的顺序出了问题（交叉依赖）， 网上示例代码很多，比如搜索“Java 死锁 示例”。</p>
<p>在 Linux 和 macOS 上，<code>jstack pid</code> 的效果跟 <code>kill -3 pid</code> 相同。</p>
<h3>jinfo 工具</h3>
<p>诊断工具：jinfo 用来查看具体生效的配置信息以及系统属性，还支持动态增加一部分参数。</p>
<p>看看帮助信息：</p>
<blockquote>
<p>$ <code>jinfo -help</code></p>
</blockquote>
<pre><code>Usage:
    jinfo [option] &lt;pid&gt;
        (to connect to running process)
    jinfo [option] &lt;executable &lt;core&gt;
        (to connect to a core file)
    jinfo [option] [<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fe8d9b8c889b8ca1979abe">[email&#160;protected]</a>]&lt;remote-IP-hostname&gt;
        (to connect to remote debug server)

where &lt;option&gt; is one of:
    -flag &lt;name&gt;         to print the value of the named VM flag
    -flag [+|-]&lt;name&gt;    to enable or disable the named VM flag
    -flag &lt;name&gt;=&lt;value&gt; to set the named VM flag to the given value
    -flags               to print VM flags
    -sysprops            to print Java system properties
    &lt;no option&gt;          to print both of the above
    -h | -help           to print this help message

</code></pre>
<p>使用示例：</p>
<pre><code>jinfo 36663
jinfo -flags 36663

</code></pre>
<p>不加参数过滤，则打印所有信息。</p>
<p>jinfo 在 Windows 上比较稳定。在 macOS 上需要 root 权限，或是需要在提示下输入当前用户的密码。</p>
<p><img src="assets/780663e0-2608-11ea-aa89-e1cacb5bf377" alt="56345767.png" /></p>
<p>然后就可以看到如下信息：</p>
<pre><code>jinfo 36663
Attaching to process ID 36663, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.131-b11
Java System Properties:

java.runtime.name = Java(TM) SE Runtime Environment
java.vm.version = 25.131-b11
sun.boot.library.path = /Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib
// 中间省略了几十行
java.ext.dirs = /Users/kimmking/Library/Java/Extensions:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/ext:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java
sun.boot.class.path = /Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/resources.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/rt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/sunrsasign.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/jsse.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/jce.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/charsets.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/jfr.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/classes
java.vendor = Oracle Corporation
maven.home = /Users/kimmking/tools/apache-maven-3.5.0
file.separator = /
java.vendor.url.bug = http://bugreport.sun.com/bugreport/
sun.io.unicode.encoding = UnicodeBig
sun.cpu.endian = little
sun.cpu.isalist =

VM Flags:
Non-default VM flags: -XX:CICompilerCount=3 -XX:InitialHeapSize=134217728 -XX:MaxHeapSize=2147483648 -XX:MaxNewSize=715653120 -XX:MinHeapDeltaBytes=524288 -XX:NewSize=44564480 -XX:OldSize=89653248 -XX:+TraceClassLoading -XX:+TraceClassUnloading -XX:+UseCompressedClassPointers -XX:+UseCompressedOops -XX:+UseFastUnorderedTimeStamps -XX:+UseParallelGC
Command line: -Dclassworlds.conf=/Users/kimmking/tools/apache-maven-3.5.0/bin/m2.conf -Dmaven.home=/Users/kimmking/tools/apache-maven-3.5.0 -Dmaven.multiModuleProjectDirectory=/Users/kimmking/gateway/spring-cloud-gateway-demo/netty-server

</code></pre>
<p>可以看到所有的系统属性和启动使用的 VM 参数、命令行参数。非常有利于我们排查问题，特别是去排查一个已经运行的 JVM 里问题，通过 jinfo 我们就知道它依赖了哪些库，用了哪些参数启动。</p>
<p>如果在 Mac 和 Linux 系统上使用一直报错，则可能是没有权限，或者 jinfo 版本和目标 JVM 版本不一致的原因，例如：</p>
<pre><code>Error attaching to process:
  sun.jvm.hotspot.runtime.VMVersionMismatchException:
    Supported versions are 25.74-b02. Target VM is 25.66-b17

</code></pre>
<h3>jrunscript 和 jjs 工具</h3>
<p>jrunscript 和 jjs 工具用来执行脚本，只要安装了 JDK 8+，就可以像 shell 命令一样执行相关的操作了。这两个工具背后，都是 JDK 8 自带的 JavaScript 引擎 Nashorn。</p>
<p>执行交互式操作：</p>
<pre><code>$ jrunscript
nashorn&gt; 66+88
154

</code></pre>
<p>或者：</p>
<pre><code>$ jjs
jjs&gt; 66+88
154

</code></pre>
<p>按 CTRL+C 或者输入 exit() 回车，退出交互式命令行。</p>
<p>其中 jrunscript 可以直接用来执行 JS 代码块或 JS 文件。比如类似 curl 这样的操作：</p>
<pre><code class="language-shell">jrunscript -e &quot;cat('http://www.baidu.com')&quot;

</code></pre>
<p>或者这样：</p>
<pre><code class="language-shell">jrunscript -e &quot;print('hello,kk.jvm'+1)&quot;

</code></pre>
<p>甚至可以执行 JS 脚本：</p>
<pre><code>jrunscript -l js -f /XXX/XXX/test.js

</code></pre>
<p>而 jjs 则只能交互模式，但是可以指定 JavaScript 支持的 ECMAScript 语言版本，比如 ES5 或者 ES6。</p>
<p>这个工具在某些情况下还是有用的，还可以在脚本中执行 Java 代码，或者调用用户自己的 jar 文件或者 Java 类。详细的操作说明可以参考：</p>
<blockquote>
<p><a href="https://docs.oracle.com/javase/7/docs/technotes/tools/share/jrunscript.html">jrunscript - command line script shell</a></p>
</blockquote>
<p>如果是 JDK 9 及以上的版本，则有一个更完善的 REPL 工具——JShell，可以直接解释执行 Java 代码。</p>
<p>而这些性能诊断工具官方并不提供技术支持，所以如果碰到报错信息，请不要着急，可以试试其他工具。不行就换 JDK 版本。</p>
<h3>参考文档</h3>
<ul>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/tools/index.html">JDK 内置程序和工具</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;JVM&#32;启动参数详解：博观而约取、厚积而薄发.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;JDK&#32;内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340b81fa070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
