<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>35  Truffle：语言实现框架.md</title>
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

                    
                    <a href="34&#32;&#32;Graal：用Java编译Java.md">34  Graal：用Java编译Java.md</a>

                </li>
                <li>

                    <a class="current-tab" href="35&#32;&#32;Truffle：语言实现框架.md">35  Truffle：语言实现框架.md</a>
                    

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
                        <div><h1>35  Truffle：语言实现框架</h1>
<p>今天我们来聊聊 GraalVM 中的语言实现框架 Truffle。</p>
<p>我们知道，实现一门新编程语言的传统做法是实现一个编译器，也就是把用该语言编写的程序转换成可直接在硬件上运行的机器码。</p>
<p>通常来说，编译器分为前端和后端：前端负责词法分析、语法分析、类型检查和中间代码生成，后端负责编译优化和目标代码生成。</p>
<p>不过，许多编译器教程只涉及了前端中的词法分析和语法分析，并没有真正生成可以运行的目标代码，更谈不上编译优化，因此在生产环境中并不实用。</p>
<p>另一种比较取巧的做法则是将新语言编译成某种已知语言，或者已知的中间形式，例如将 Scala、Kotlin 编译成 Java 字节码。</p>
<p>这样做的好处是可以直接享用 Java 虚拟机自带的各项优化，包括即时编译、自动内存管理等等。因此，这种做法对所生成的 Java 字节码的优化程度要求不高。</p>
<p>不过，不管是附带编译优化的编译器，还是生成中间形式并依赖于其他运行时的即时编译优化的编译器，它们所针对的都是<a href="https://en.wikipedia.org/wiki/Compiled_language">编译型语言</a>，在运行之前都需要这一额外的编译步骤。</p>
<p>与编译型语言相对应的则是<a href="https://en.wikipedia.org/wiki/Interpreted_language">解释型语言</a>，例如 JavaScript、Ruby、Python 等。对于这些语言来说，它们无须额外的编译步骤，而是依赖于解释执行器进行解析并执行。</p>
<p>为了让该解释执行器能够高效地运行大型程序，语言实现开发人员通常会将其包装在虚拟机里，并实现诸如即时编译、垃圾回收等其他组件。这些组件对语言设计 本身并无太大贡献，仅仅是为了实用性而不得不进行的工程实现。</p>
<p>在理想情况下，我们希望在不同的语言实现中复用这些组件。也就是说，每当开发一门新语言时，我们只需要实现它的解释执行器，便能够直接复用即时编译、垃圾回收等组件，从而达到高性能的效果。这也是 Truffle 项目的目标。接下来，我们就来讲讲这个项目。</p>
<h2>Truffle 项目简介</h2>
<p>Truffle 是一个用 Java 写就的语言实现框架。基于 Truffle 的语言实现仅需用 Java 实现词法分析、语法分析以及针对语法分析所生成的抽象语法树（Abstract Syntax Tree，AST）的解释执行器，便可以享用由 Truffle 提供的各项运行时优化。</p>
<p>就一个完整的 Truffle 语言实现而言，由于实现本身以及其所依赖的 Truffle 框架部分都是用 Java 实现的，因此它可以运行在任何 Java 虚拟机之上。</p>
<p>当然，如果 Truffle 运行在附带了 Graal 编译器的 Java 虚拟机之上，那么它将调用 Graal 编译器所提供的 API，主动触发对 Truffle 语言的即时编译，将对 AST 的解释执行转换为执行即时编译后的机器码。</p>
<p>在这种情况下，Graal 编译器相当于一个提供了即时编译功能的库，宿主虚拟机本身仍可使用 C2 作为其唯一的即时编译器，或者分层编译模式下的 4 层编译器。</p>
<p><img src="assets/20c7a514f226689536fafc6886a08e30.png" alt="img" /></p>
<p>我们团队实现并且开源了多个 Truffle 语言，例如<a href="https://github.com/graalvm/graaljs">JavaScript</a>，<a href="https://github.com/oracle/truffleruby">Ruby</a>，<a href="https://github.com/oracle/fastr">R</a>，<a href="https://github.com/graalvm/graalpython">Python</a>，以及可用来解释执行 LLVM bitcode 的<a href="https://github.com/oracle/graal/tree/master/sulong">Sulong</a>。关于 Sulong 项目，任何能够编译为 LLVM bitcode 的编程语言，例如 C/C++，都能够在这上面运行。</p>
<p>下图展示了运行在 GraalVM EE 上的 Java 虚拟机语言，以及除 Python 外 Truffle 语言的峰值性能指标（2017 年数据）。</p>
<p><img src="assets/0aa87b77b2d6eb0147d4a2b342b0d644.png" alt="img" /></p>
<p>这里我采用的基线是每个语言较有竞争力的语言实现。</p>
<ul>
<li>对于 Java 虚拟机语言（Java、Scala），我比较的是使用 C2 的 HotSpot 虚拟机和使用 Graal 的 HotSpot 虚拟机。</li>
<li>对于 Ruby，我比较的是运行在 HotSpot 虚拟机之上的 JRuby 和 Truffle Ruby。</li>
<li>对于 R，我比较的是 GNU R 和基于 Truffle 的 FastR。</li>
<li>对于 C/C++，我比较的是利用 LLVM 编译器生成的二进制文件和基于 Truffle 的 Sulong。</li>
<li>对于 JavaScript，我比较的是 Google 的 V8 和 Graal.js。</li>
</ul>
<p>针对每种语言，我们运行了上百个基准测试，求出各个基准测试<strong>峰值性能</strong>的加速比，并且汇总成图中所示的几何平均值（Geo. mean）。</p>
<p>简单地说明一下，当 GraalVM 的加速比为 1 时，代表使用其他语言实现和使用 GraalVM 的性能相当。当 GraalVM 加速比超过 1 时，则代表 GraalVM 的性能较好；反之，则说明 GraalVM 的性能较差。</p>
<p>我们可以看到，Java 跑在 Graal 上和跑在 C2 上的执行效率类似，而 Scala 跑在 Graal 上的执行效率则是跑在 C2 上的 1.2 倍。</p>
<p>对于 Ruby 或者 R 这类解释型语言，经由 Graal 编译器加速的 Truffle 语言解释器的性能十分优越，分别达到对应基线的 4.1x 和 4.5x。这里便可以看出使用专业即时编译器的 Truffle 框架的优势所在。</p>
<p>不过，对于同样拥有专业即时编译器的 V8 来说，基于 Truffle 的 Graal.js 仍处于追赶者的位置。考虑到我们团队中负责 Graal.js 的工程师仅有个位数，能够达到如此性能已属不易。现在 Graal.js 已经开源出来，我相信借助社区的贡献，它的性能能够得到进一步的提升。</p>
<p>Sulong 与传统的 C/C++ 相比，由于两者最终都将编译为机器码，因此原则上后者定义了前者的性能上限。</p>
<p>不过，Sulong 将 C/C++ 代码放在托管环境中运行，所有代码中的内存访问都会在托管环境的监控之下。无论是会触发 Segfault 的异常访问，还是读取敏感数据的恶意访问，都能够被 Sulong 拦截下来并作出相应处理。</p>
<h2>Partial Evaluation</h2>
<p>如果要理解 Truffle 的原理，我们需要先了解 Partial Evaluation 这一个概念。</p>
<p>假设有一段程序<code>P</code>，它将一系列输入<code>I</code>转换成输出<code>O</code>（即<code>P: I -&gt; O</code>）。而这些输入又可以进一步划分为编译时已知的常量<code>IS</code>，和编译时未知的<code>ID</code>。</p>
<p>那么，我们可以将程序<code>P: I -&gt; O</code>转换为等价的另一段程序<code>P': ID -&gt; O</code>。这个新程序<code>P'</code>便是<code>P</code>的特化（Specialization），而从<code>P</code>转换到<code>P'</code>的这个过程便是所谓的 Partial Evaluation。</p>
<p>回到 Truffle 这边，我们可以将 Truffle 语言的解释执行器当成<code>P</code>，将某段用 Truffle 语言写就的程序当作<code>IS</code>，并通过 Partial Evaluation 特化为<code>P'</code>。由于 Truffle 语言的解释执行器是用 Java 写的，因此我们可以利用 Graal 编译器将<code>P'</code>编译为二进制码。</p>
<p>下面我将用一个具体例子来讲解。</p>
<p>假设有一门语言 X，只支持读取整数参数和整数加法。这两种操作分别对应下面这段代码中的 AST 节点<code>Arg</code>和<code>Add</code>。</p>
<pre><code>abstract class Node {
  abstract int execute(int[] args);
}
 
class Arg extends Node {
  final int index;
 
  Arg(int i) { this.index = i; }
 
  int execute(int[] args) {
    return args[index];
  }
}
 
class Add extends Node {
  final Node left, right;
 
  Add(Node left, Node right) {
    this.left = left;
    this.right = right;
  }
 
  int execute(int[] args) {
    return left.execute(args) +
           right.execute(args);
  }
}
 
static int interpret(Node node, int[] args) {
  return node.execute(args);
}
</code></pre>
<p>所谓 AST 节点的解释执行，便是调用这些 AST 节点的<code>execute</code>方法；而一段程序的解释执行，则是调用这段程序的 AST 根节点的<code>execute</code>方法。</p>
<p>我们可以看到，<code>Arg</code>节点和<code>Add</code>节点均实现了<code>execute</code>方法，接收一个用来指代程序输入的 int 数组参数，并返回计算结果。其中，<code>Arg</code>节点将返回 int 数组的第<code>i</code>个参数（<code>i</code>是硬编码在程序之中的常量）；而<code>Add</code>节点将分别调用左右两个节点的<code>execute</code>方法， 并将所返回的值相加后再返回。</p>
<p>下面我们将利用语言 X 实现一段程序，计算三个输入参数之和<code>arg0 + arg1 + arg2</code>。这段程序解析生成的 AST 如下述代码所示：</p>
<pre><code>// Sample program: arg0 + arg1 + arg2
sample = new Add(new Add(new Arg(0), new Arg(1)), new Arg(2));
</code></pre>
<p>这段程序对应的解释执行则是<code>interpret(sample, args)</code>，其中<code>args</code>为代表传入参数的 int 数组。由于<code>sample</code>是编译时常量，因此我们可以将其通过 Partial Evaluation，特化为下面这段代码所示的<code>interpret0</code>方法：</p>
<pre><code>static final Node sample = new Add(new Add(new Arg(0), new Arg(1)), new Arg(2));
 
static int interpret0(int[] args) {
  return sample.execute(args);
}
</code></pre>
<p>Truffle 的 Partial Evaluator 会不断进行方法内联（直至遇到被``@TruffleBoundary<code>注解的方法）。因此，上面这段代码的</code>interpret0<code>方法，在内联了对</code>Add.execute`方法的调用之后，会转换成下述代码：</p>
<pre><code>static final Node sample = new Add(new Add(new Arg(0), new Arg(1)), new Arg(2));
 
static int interpret0(int[] args) {
  return sample.left.execute(args) + sample.right.execute(args);
}
</code></pre>
<p>同样，我们可以进一步内联对<code>Add.execute</code>方法的调用以及对<code>Arg.execute</code>方法的调用，最终将<code>interpret0</code>转换成下述代码：</p>
<pre><code>static int interpret0(int[] args) {
  return args[0] + args[1] + args[2];
}
</code></pre>
<p>至此，我们已成功地将一段 Truffle 语言代码的解释执行转换为上述 Java 代码。接下来，我们便可以让 Graal 编译器将这段 Java 代码编译为机器码，从而实现 Truffle 语言的即时编译。</p>
<h2>节点重写</h2>
<p>Truffle 的另一项关键优化是节点重写（node rewriting）。</p>
<p>在动态语言中，许多变量的类型是在运行过程中方能确定的。以加法符号<code>+</code>为例，它既可以表示整数加法，还可以表示浮点数加法，甚至可以表示字符串加法。</p>
<p>如果是静态语言，我们可以通过推断加法的两个操作数的具体类型，来确定该加法的类型。但对于动态语言来说，我们需要在运行时动态确定操作数的具体类型，并据此选择对应的加法操作。这种在运行时选择语义的节点，会十分不利于即时编译，从而严重影响到程序的性能。</p>
<p>Truffle 语言解释器会收集每个 AST 节点所代表的操作的类型，并且在即时编译时，作出针对所收集得到的类型 profile 的特化（specialization）。</p>
<p>还是以加法操作为例，如果所收集的类型 profile 显示这是一个整数加法操作，那么在即时编译时我们会将对应的 AST 节点当成整数加法；如果是一个字符串加法操作，那么我们会将对应的 AST 节点当成字符串加法。</p>
<p>当然，如果该加法操作既有可能是整数加法也可能是字符串加法，那么我们只好在运行过程中判断具体的操作类型，并选择相应的加法操作。</p>
<p><img src="assets/543ee374164fd43f2773043c675b568f.png" alt="img" /></p>
<p>这种基于类型 profile 的优化，与我们以前介绍过的 Java 虚拟机中解释执行器以及三层 C1 编译代码十分类似，它们背后的核心都是基于假设的投机性优化，以及在假设失败时的去优化。</p>
<p>在即时编译过后，如果运行过程中发现 AST 节点的实际类型和所假设的类型不同，Truffle 会主动调用 Graal 编译器提供的去优化 API，返回至解释执行 AST 节点的状态，并且重新收集 AST 节点的类型信息。之后，Truffle 会再次利用 Graal 编译器进行新一轮的即时编译。</p>
<p>当然，如果能够在第一次编译时便已达到稳定状态，不再触发去优化以及重新编译，那么，这会极大地减短程序到达峰值性能的时间。为此，我们统计了各个 Truffle 语言的方法在进行过多少次方法调用后，其 AST 节点的类型会固定下来。</p>
<p>据统计，在 JavaScript 方法和 Ruby 方法中，80% 会在 5 次方法调用后稳定下来，90% 会在 7 次调用后稳定下来，99% 会在 19 次方法调用之后稳定下来。</p>
<p>R 语言的方法则比较特殊，即便是不进行任何调用，有 50% 的方法已经稳定下来了。这背后的原因也不难推测，这是因为 R 语言主要用于数值统计，几乎所有的操作都是浮点数类型的。</p>
<h2>Polyglot</h2>
<p>在开发过程中，我们通常会为工程项目选定一门语言，但问题也会接踵而至：一是这门语言没有实现我们可能需要用到的库，二是这门语言并不适用于某类问题。</p>
<p>Truffle 语言实现框架则支持 Polyglot，允许在同一段代码中混用不同的编程语言，从而使得开发人员能够自由地选择合适的语言来实现子组件。</p>
<p>与其他 Polyglot 框架不同的是，Truffle 语言之间能够共用对象。也就是说，在不对某个语言中的对象进行复制或者序列化反序列化的情况下，Truffle 可以无缝地将该对象传递给另一门语言。因此，Truffle 的 Polyglot 在切换语言时，性能开销非常小，甚至经常能够达到零开销。</p>
<p>Truffle 的 Polyglot 特性是通过 Polyglot API 来实现的。每个实现了 Polyglot API 的 Truffle 语言，其对象都能够被其他 Truffle 语言通过 Polyglot API 解析。实际上，当通过 Polyglot API 解析外来对象时，我们并不需要了解对方语言，便能够识别其数据结构，访问其中的数据，并进行进一步的计算。</p>
<h2>总结与实践</h2>
<p>今天我介绍了 GraalVM 中的 Truffle 项目。</p>
<p>Truffle 是一个语言实现框架，允许语言开发者在仅实现词法解析、语法解析以及 AST 解释器的情况下，达到极佳的性能。目前 Oracle Labs 已经实现并维护了 JavaScript、Ruby、R、Python 以及可用于解析 LLVM bitcode 的 Sulong。后者将支持在 GraalVM 上运行 C/C++ 代码。</p>
<p>Truffle 背后所依赖的技术是 Partial Evaluation 以及节点重写。Partial Evaluation 指的是将所要编译的目标程序解析生成的抽象语法树当做编译时常量，特化该 Truffle 语言的解释器，从而得到指代这段程序解释执行过程的 Java 代码。然后，我们可以借助 Graal 编译器将这段 Java 代码即时编译为机器码。</p>
<p>节点重写则是收集 AST 节点的类型，根据所收集的类型 profile 进行的特化，并在节点类型不匹配时进行去优化并重新收集、编译的一项技术。</p>
<p>Truffle 的 Polyglot 特性支持在一段代码中混用多种不同的语言。与其他 Polyglot 框架相比，它支持在不同的 Truffle 语言中复用内存中存储的同一个对象。</p>
<hr />
<p>今天的实践环节，请你试用 GraalVM 中附带的各项语言实现。你可以运行我们官网上的各个<a href="https://www.graalvm.org/docs/examples/">示例程序</a>。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="34&#32;&#32;Graal：用Java编译Java.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="36&#32;&#32;SubstrateVM：AOT编译框架.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4358367eb3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
