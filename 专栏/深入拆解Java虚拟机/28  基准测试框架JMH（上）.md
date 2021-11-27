<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>28  基准测试框架JMH（上）.md</title>
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

                    <a class="current-tab" href="28&#32;&#32;基准测试框架JMH（上）.md">28  基准测试框架JMH（上）.md</a>
                    

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

                    
                    <a href="34&#32;&#32;Graal：用Java编译Java.md">34  Graal：用Java编译Java.md</a>

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
                        <div><h1>28  基准测试框架JMH（上）</h1>
<p>今天我们来聊聊性能基准测试（benchmarking）。</p>
<p>大家或许都看到过一些不严谨的性能测试，以及基于这些测试结果得出的令人匪夷所思的结论。</p>
<pre><code>static int foo() {
  int i = 0;
  while (i &lt; 1_000_000_000) {
    i++;
  }
  return i;
}
</code></pre>
<p>举个例子，上面这段代码中的<code>foo</code>方法，将进行 10^9 次加法操作及跳转操作。</p>
<p>不少开发人员，包括我在介绍反射调用那一篇中所做的性能测试，都使用了下面这段代码的测量方式，即通过<code>System.nanoTime</code>或者<code>System.currentTimeMillis</code>来测量每若干个操作（如连续调用 1000 次<code>foo</code>方法）所花费的时间。</p>
<pre><code>public class LoopPerformanceTest {
  static int foo() { ... }
 
  public static void main(String[] args) {
    // warmup
    for (int i = 0; i &lt; 20_000; i++) {
      foo();
    }
    // measurement
    long current = System.nanoTime();
    for (int i = 1; i &lt;= 10_000; i++) {
      foo();
      if (i % 1000 == 0) {
        long temp = System.nanoTime();
        System.out.println(temp - current);
        current = System.nanoTime();
      }
    }
  }
}
</code></pre>
<p>这种测量方式实际上过于理性化，忽略了 Java 虚拟机、操作系统，乃至硬件系统所带来的影响。</p>
<h2>性能测试的坑</h2>
<p>关于 Java 虚拟机所带来的影响，我们在前面的篇章中已经介绍过不少，如 Java 虚拟机堆空间的自适配，即时编译等。</p>
<p>在上面这段代码中，真正进行测试的代码（即<code>// measurement</code>后的代码）由于循环次数不多，属于冷循环，没有能触发 OSR 编译。</p>
<p>也就是说，我们会在<code>main</code>方法中解释执行，然后调用<code>foo</code>方法即时编译生成的机器码中。这种混杂了解释执行以及即时编译生成代码的测量方式，其得到的数据含义不明。</p>
<p>有同学认为，我们可以假设<code>foo</code>方法耗时较长（毕竟 10^9 次加法），因此<code>main</code>方法的解释执行并不会对最终计算得出的性能数据造成太大影响。上面这段代码在我的机器上测出的结果是，每 1000 次<code>foo</code>方法调用在 20 微秒左右。</p>
<p>这是否意味着，我这台机器的 CPU 已经远超它的物理限制，其频率达到 100,000,000 GHz 了。（假设循环主体就两条指令，每时钟周期指令数 [1] 为 1。）这显然是不可能的，目前 CPU 单核的频率大概在 2-5 GHz 左右，再怎么超频也不可能提升七八个数量级。</p>
<p>你应该能够猜到，这和即时编译器的循环优化有关。下面便是<code>foo</code>方法的编译结果。我们可以看到，它将直接返回 10^9，而不是循环 10^9 次，并在循环中重复进行加法。</p>
<pre><code>0x8aa0: sub    rsp,0x18                 // 创建方法栈桢
0x8aa7: mov    QWORD PTR [rsp+0x10],rbp // 无关指令
0x8aac: mov    eax,0x3b9aca00           // return 10^9
0x8ab1: add    rsp,0x10                 // 弹出方法栈桢
0x8ab5: pop    rbp                      // 无关指令
0x8ab6: mov    r10,QWORD PTR [r15+0x70] // 安全点测试
0x8aba: test   DWORD PTR [r10],eax      // 安全点测试
0x8abd: ret
</code></pre>
<blockquote>
<p>之前我忘记解释所谓的”无关指令“是什么意思。我指的是该指令和具体的代码逻辑无关。即时编译器生成的代码可能会将 RBP 寄存器作为通用寄存器，从而是寄存器分配算法有更多的选择。由于调用者（caller）未必保存了 RBP 寄存器的值，所以即时编译器会在进入被调用者（callee）时保存 RBP 的值，并在退出被调用者时复原 RBP 的值。</p>
</blockquote>
<pre><code>static int foo() {
  int i = 0;
  while (i &lt; 1_000_000_000) {
    i++;
  }
  return i;
}
// 优化为
static int foo() {
  return 1_000_000_000;
}
</code></pre>
<p>该循环优化并非循环展开。在默认情况下，即时编译器仅能将循环展开 60 次（对应虚拟机参数<code>-XX:LoopUnrollLimit</code>）。实际上，在介绍循环优化那篇文章中，我并没有提及这个优化。因为该优化实在是太过于简单，几乎所有开发人员都能够手工对其进行优化。</p>
<p>在即时编译器中，它是一个基于计数循环的优化。我们也已经学过计数循环的知识。也就是说，只要将循环变量<code>i</code>改为 long 类型，便可以“避免”这个优化。</p>
<p>关于操作系统和硬件系统所带来的影响，一个较为常见的例子便是电源管理策略。在许多机器，特别是笔记本上，操作系统会动态配置 CPU 的频率。而 CPU 的频率又直接影响到性能测试的数据，因此短时间的性能测试得出的数据未必可靠。</p>
<p><img src="assets/07ca617893718782b8eb58344b7bb097.jpeg" alt="img" /></p>
<p>例如我的笔记本，在刚开始进行性能评测时，单核频率可以达到 4.0 GHz。而后由于 CPU 温度升高，频率便被限制在 3.0 GHz 了。</p>
<p>除了电源管理之外，CPU 缓存、分支预测器 [2]，以及超线程技术 [3]，都会对测试结果造成影响。</p>
<p>就 CPU 缓存而言，如果程序的数据本地性较好，那么它的性能指标便会非常好；如果程序存在 false sharing 的问题，即几个线程写入内存中属于同一缓存行的不同部分，那么它的性能指标便会非常糟糕。</p>
<p>超线程技术是另一个可能误导性能测试工具的因素。我们知道，超线程技术将为每个物理核心虚拟出两个虚拟核心，从而尽可能地提高物理核心的利用率。如果性能测试的两个线程被安排在同一物理核心上，那么得到的测试数据显然要比被安排在不同物理核心上的数据糟糕得多。</p>
<p>总而言之，性能基准测试存在着许多深坑（pitfall）。然而，除了性能测试专家外，大多数开发人员都没有足够全面的知识，能够绕开这些坑，因而得出的性能测试数据很有可能是有偏差的（biased）。</p>
<p>下面我将介绍 OpenJDK 中的开源项目 JMH[4]（Java Microbenchmark Harness）。JMH 是一个面向 Java 语言或者其他 Java 虚拟机语言的性能基准测试框架。它针对的是纳秒级别（出自官网介绍，个人觉得精确度没那么高）、微秒级别、毫秒级别，以及秒级别的性能测试。</p>
<p>由于许多即时编译器的开发人员参与了该项目，因此 JMH 内置了许多功能来控制即时编译器的优化。对于其他影响性能评测的因素，JMH 也提供了不少策略来降低影响，甚至是彻底解决。</p>
<p>因此，使用这个性能基准测试框架的开发人员，可以将精力完全集中在所要测试的业务逻辑，并以最小的代价控制除了业务逻辑之外的可能影响性能的因素。</p>
<pre><code>REMEMBER: The numbers below are just data. To gain reusable insights, you need to follow up on why the numbers are the way they are. Use profilers (see -prof, -lprof), design factorial experiments, perform baseline and negative tests that provide experimental control, make sure the benchmarking environment is safe on JVM/OS/HW level, ask for reviews from the domain experts. Do not assume the numbers tell you what you want them to tell.
</code></pre>
<p>不过，JMH 也不能完美解决性能测试数据的偏差问题。它甚至会在每次运行的输出结果中打印上述语句，所以，JMH 的开发人员也给出了一个小忠告：我们开发人员不要轻信 JMH 的性能测试数据，不要基于这些数据乱下结论。</p>
<p>通常来说，性能基准测试的结果反映的是所测试的业务逻辑在所运行的 Java 虚拟机，操作系统，硬件系统这一组合上的性能指标，而根据这些性能指标得出的通用结论则需要经过严格论证。</p>
<p>在理解（或忽略）了 JMH 的忠告后，我们下面便来看看如何使用 JMH。</p>
<h2>生成 JMH 项目</h2>
<p>JMH 的使用方式并不复杂。我们可以借助 JMH 部署在 maven 上的 archetype，生成预设好依赖关系的 maven 项目模板。具体的命令如下所示：</p>
<pre><code>$ mvn archetype:generate \
          -DinteractiveMode=false \
          -DarchetypeGroupId=org.openjdk.jmh \
          -DarchetypeArtifactId=jmh-java-benchmark-archetype \
          -DgroupId=org.sample \
          -DartifactId=test \
          -Dversion=1.21
$ cd test
</code></pre>
<p>该命令将在当前目录下生成一个<code>test</code>文件夹（对应参数<code>-DartifactId=test</code>，可更改），其中便包含了定义该 maven 项目依赖的<code>pom.xml</code>文件，以及自动生成的测试文件<code>src/main/org/sample/MyBenchmark.java</code>（这里<code>org/sample</code>对应参数<code>-DgroupId=org.sample</code>，可更改）。后者的内容如下所示：</p>
<pre><code>/*
 * Copyright ...
 */
package org.sample;
 
import org.openjdk.jmh.annotations.Benchmark;
 
public class MyBenchmark {
 
    @Benchmark
    public void testMethod() {
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }
 
}
</code></pre>
<p>这里面，类名<code>MyBenchmark</code>以及方法名<code>testMethod</code>并不重要，你可以随意更改。真正重要的是<code>@Benchmark</code>注解。被它标注的方法，便是 JMH 基准测试的测试方法。该测试方法默认是空的。我们可以填入需要进行性能测试的业务逻辑。</p>
<p>举个例子，我们可以测量新建异常对象的性能，如下述代码所示：</p>
<pre><code>@Benchmark
public void testMethod() {
  new Exception();
}
</code></pre>
<p>通常来说，我们不应该使用这种貌似会被即时编译器优化掉的代码（在下篇中我会介绍 JMH 的<code>Blackhole</code>功能）。</p>
<p>不过，我们已经学习过逃逸分析了，知道 native 方法调用的调用者或者参数会被识别为逃逸。而<code>Exception</code>的构造器将间接调用至 native 方法<code>fillInStackTrace</code>中，并且该方法调用的调用者便是新建的<code>Exception</code>对象。因此，逃逸分析将判定该新建对象逃逸，而即时编译器也无法优化掉原本的新建对象操作。</p>
<p>当<code>Exception</code>的构造器返回时，Java 虚拟机将不再拥有指向这一新建对象的引用。因此，该新建对象可以被垃圾回收。</p>
<h2>编译和运行 JMH 项目</h2>
<p>在上一篇介绍注解处理器时，我曾提到过，JMH 正是利用注解处理器 [5] 来自动生成性能测试的代码。实际上，除了<code>@Benchmark</code>之外，JMH 的注解处理器还将处理所有位于<code>org.openjdk.jmh.annotations</code>包 [6] 下的注解。（其他注解我们会在下一篇中详细介绍。）</p>
<p>我们可以运行<code>mvn compile</code>命令来编译这个 maven 项目。该命令将生成<code>target</code>文件夹，其中的<code>generated-sources</code>目录便存放着由 JMH 的注解处理器所生成的 Java 源代码：</p>
<pre><code>$ mvn compile
$ ls target/generated-sources/annotations/org/sample/generated/
MyBenchmark_jmhType.java            MyBenchmark_jmhType_B1.java         MyBenchmark_jmhType_B2.java         MyBenchmark_jmhType_B3.java         MyBenchmark_testMethod_jmhTest.java
</code></pre>
<p>在这些源代码里，所有以<code>MyBenchmark_jmhType</code>为前缀的 Java 类都继承自<code>MyBenchmark</code>。这是注解处理器的常见用法，即通过生成子类来将注解所带来的额外语义扩张成方法。</p>
<p>具体来说，它们之间的继承关系是<code>MyBenchmark_jmhType -&gt; B3 -&gt; B2 -&gt; B1 -&gt; MyBenchmark</code>（这里<code>A -&gt; B</code>代表 A 继承 B）。其中，B2 存放着 JMH 用来控制基准测试的各项字段。</p>
<p>为了避免这些控制字段对<code>MyBenchmark</code>类中的字段造成 false sharing 的影响，JMH 生成了 B1 和 B3，分别存放了 256 个 boolean 字段，从而避免 B2 中的字段与<code>MyBenchmark</code>类、<code>MyBenchmark_jmhType</code>类中的字段（或内存里下一个对象中的字段）会出现在同一缓存行中。</p>
<blockquote>
<p>之所以不能在同一类中安排这些字段，是因为 Java 虚拟机的字段重排列。而类之间的继承关系，便可以避免不同类所包含的字段之间的重排列。</p>
</blockquote>
<p>除了这些<code>jmhType</code>源代码外，<code>generated-sources</code>目录还存放着真正的性能测试代码<code>MyBenchmark_testMethod_jmhTest.java</code>。当进行性能测试时，Java 虚拟机所运行的代码很有可能便是这一个源文件中的热循环经过 OSR 编译过后的代码。</p>
<blockquote>
<p>在通过 CompileCommand 分析即时编译后的机器码时，我们需要关注的其实是<code>MyBenchmark_testMethod_jmhTest</code>中的方法。</p>
</blockquote>
<p>由于这里面的内容过于复杂，我将在下一篇中介绍影响该生成代码的众多功能性注解，这里就不再详细进行介绍了。</p>
<p>接下来，我们可以运行<code>mvn package</code>命令，将编译好的 class 文件打包成 jar 包。生成的 jar 包同样位于<code>target</code>目录下，其名字为<code>benchmarks.jar</code>。jar 包里附带了一系列配置文件，如下所示：</p>
<pre><code>$ mvn package
 
$ jar tf target/benchmarks.jar META-INF
META-INF/MANIFEST.MF
META-INF/
META-INF/BenchmarkList
META-INF/CompilerHints
META-INF/maven/
META-INF/maven/org.sample/
META-INF/maven/org.sample/test/
META-INF/maven/org.sample/test/pom.xml
META-INF/maven/org.sample/test/pom.properties
META-INF/maven/org.openjdk.jmh/
META-INF/maven/org.openjdk.jmh/jmh-core/
META-INF/maven/org.openjdk.jmh/jmh-core/pom.xml
META-INF/maven/org.openjdk.jmh/jmh-core/pom.properties
META-INF/maven/net.sf.jopt-simple/
META-INF/maven/net.sf.jopt-simple/jopt-simple/
META-INF/maven/net.sf.jopt-simple/jopt-simple/pom.xml
META-INF/maven/net.sf.jopt-simple/jopt-simple/pom.properties
META-INF/LICENSE.txt
META-INF/NOTICE.txt
META-INF/maven/org.apache.commons/
META-INF/maven/org.apache.commons/commons-math3/
META-INF/maven/org.apache.commons/commons-math3/pom.xml
META-INF/maven/org.apache.commons/commons-math3/pom.properties
 
$ unzip -c target/benchmarks.jar META-INF/MANIFEST.MF
Archive:  target/benchmarks.jar
  inflating: META-INF/MANIFEST.MF    
Manifest-Version: 1.0
Archiver-Version: Plexus Archiver
Created-By: Apache Maven 3.5.4
Built-By: zhengy
Build-Jdk: 10.0.2
Main-Class: org.openjdk.jmh.Main
 
$ unzip -c target/benchmarks.jar META-INF/BenchmarkList
Archive:  target/benchmarks.jar
  inflating: META-INF/BenchmarkList  
JMH S 22 org.sample.MyBenchmark S 51 org.sample.generated.MyBenchmark_testMethod_jmhTest S 10 testMethod S 10 Throughput E A 1 1 1 E E E E E E E E E E E E E E E E E
 
$ unzip -c target/benchmarks.jar META-INF/CompilerHints
Archive:  target/benchmarks.jar
  inflating: META-INF/CompilerHints  
dontinline,*.*_all_jmhStub
dontinline,*.*_avgt_jmhStub
dontinline,*.*_sample_jmhStub
dontinline,*.*_ss_jmhStub
dontinline,*.*_thrpt_jmhStub
inline,org/sample/MyBenchmark.testMethod
</code></pre>
<p>这里我展示了其中三个比较重要的配置文件。</p>
<ol>
<li><code>MANIFEST.MF</code>中指定了该 jar 包的默认入口，即<code>org.openjdk.jmh.Main</code>[7]。</li>
<li><code>BenchmarkList</code>中存放了测试配置。该配置是根据<code>MyBenchmark.java</code>里的注解自动生成的，具体我会在下一篇中详细介绍源代码中如何配置。</li>
<li><code>CompilerHints</code>中存放了传递给 Java 虚拟机的<code>-XX:CompileCommandFile</code>参数的内容。它规定了无法内联以及必须内联的几个方法，其中便有存放业务逻辑的测试方法<code>testMethod</code>。</li>
</ol>
<p>在编译<code>MyBenchmark_testMethod_jmhTest</code>类中的测试方法时，JMH 会让即时编译器强制内联对<code>MyBenchmark.testMethod</code>的方法调用，以避免调用开销。</p>
<p>打包生成的 jar 包可以直接运行。具体指令如下所示：</p>
<pre><code>$ java -jar target/benchmarks.jar
WARNING: An illegal reflective access operation has occurred
...
Benchmark                Mode  Cnt        Score      Error  Units
MyBenchmark.testMethod  thrpt   25  1004801,393 ± 4055,462  ops/s
</code></pre>
<p>这里 JMH 会有非常多的输出，具体内容我会在下一篇中进行讲解。</p>
<p>输出的最后便是本次基准测试的结果。其中比较重要的两项指标是<code>Score</code>和<code>Error</code>，分别代表本次基准测试的平均吞吐量（每秒运行<code>testMethod</code>方法的次数）以及误差范围。例如，这里的结果说明本次基准测试平均每秒生成 10^6 个异常实例，误差范围大致在 4000 个异常实例。</p>
<h2>总结与实践</h2>
<p>今天我介绍了 OpenJDK 的性能基准测试项目 JMH。</p>
<p>Java 程序的性能测试存在着许多深坑，有来自 Java 虚拟机的，有来自操作系统的，甚至有来自硬件系统的。如果没有足够的知识，那么性能测试的结果很有可能是有偏差的。</p>
<p>性能基准测试框架 JMH 是 OpenJDK 中的其中一个开源项目。它内置了许多功能，来规避由 Java 虚拟机中的即时编译器或者其他优化对性能测试造成的影响。此外，它还提供了不少策略来降低来自操作系统以及硬件系统的影响。</p>
<p>开发人员仅需将所要测试的业务逻辑通过<code>@Benchmark</code>注解，便可以让 JMH 的注解处理器自动生成真正的性能测试代码，以及相应的性能测试配置文件。</p>
<hr />
<p>今天的实践环节，请生成一个 JMH 项目，并且在<code>MyBenchmark.testMethod</code>方法中填入自己的业务逻辑。（除非你已经提前了解<code>@State</code>等 JMH 功能，否则请不要在<code>MyBenchmark</code>中定义实例变量。）</p>
<p>[1] https://en.wikipedia.org/wiki/Instructions_per_cycle
[2] https://en.wikipedia.org/wiki/Branch_predictor
[3] https://en.wikipedia.org/wiki/Hyper-threading
[4] http://openjdk.java.net/projects/code-tools/jmh/
[5] http://hg.openjdk.java.net/code-tools/jmh/file/3769055ad883/jmh-generator-annprocess/src/main/java/org/openjdk/jmh/generators/BenchmarkProcessor.java
[6] http://hg.openjdk.java.net/code-tools/jmh/file/3769055ad883/jmh-core/src/main/java/org/openjdk/jmh/annotations
[7] http://hg.openjdk.java.net/code-tools/jmh/file/3769055ad883/jmh-core/src/main/java/org/openjdk/jmh/Main.java</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="27&#32;&#32;注解处理器.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="29&#32;&#32;基准测试框架JMH（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4358020e18645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
