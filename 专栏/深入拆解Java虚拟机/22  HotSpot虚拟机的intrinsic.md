<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>22  HotSpot虚拟机的intrinsic.md</title>
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

                    <a class="current-tab" href="22&#32;&#32;HotSpot虚拟机的intrinsic.md">22  HotSpot虚拟机的intrinsic.md</a>
                    

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
                        <div><h1>22  HotSpot虚拟机的intrinsic</h1>
<p>前不久，有同学问我，<code>String.indexOf</code>方法和自己实现的<code>indexOf</code>方法在字节码层面上差不多，为什么执行效率却有天壤之别呢？今天我们就来看一看。</p>
<pre><code>public int indexOf(String str) {
    if (coder() == str.coder()) {
        return isLatin1() ? StringLatin1.indexOf(value, str.value)
                          : StringUTF16.indexOf(value, str.value);
    }
    if (coder() == LATIN1) {  // str.coder == UTF16
        return -1;
    }
    return StringUTF16.indexOfLatin1(value, str.value);
}
</code></pre>
<p>为了解答这个问题，我们来读一下<code>String.indexOf</code>方法的源代码（上面的代码截取自 Java 10.0.2）。</p>
<blockquote>
<p>在 Java 9 之前，字符串是用 char 数组来存储的，主要为了支持非英文字符。然而，大多数 Java 程序中的字符串都是由 Latin1 字符组成的。也就是说每个字符仅需占据一个字节，而使用 char 数组的存储方式将极大地浪费内存空间。</p>
<p>Java 9 引入了 Compact Strings[1] 的概念，当字符串仅包含 Latin1 字符时，使用一个字节代表一个字符的编码格式，使得内存使用效率大大提高。</p>
</blockquote>
<p>假设我们调用<code>String.indexOf</code>方法的调用者以及参数均为只包含 Latin1 字符的字符串，那么该方法的关键在于对<code>StringLatin1.indexOf</code>方法的调用。</p>
<p>下面我列举了<code>StringLatin1.indexOf</code>方法的源代码。你会发现，它并没有使用特别高明的算法，唯一值得注意的便是方法声明前的<code>@HotSpotIntrinsicCandidate</code>注解。</p>
<pre><code>@HotSpotIntrinsicCandidate
public static int indexOf(byte[] value, byte[] str) {
    if (str.length == 0) {
        return 0;
    }
    if (value.length == 0) {
        return -1;
    }
    return indexOf(value, value.length, str, str.length, 0);
}
 
@HotSpotIntrinsicCandidate
public static int indexOf(byte[] value, int valueCount, byte[] str, int strCount, int fromIndex) {
    byte first = str[0];
    int max = (valueCount - strCount);
    for (int i = fromIndex; i &lt;= max; i++) {
        // Look for first character.
        if (value[i] != first) {
            while (++i &lt;= max &amp;&amp; value[i] != first);
        }
        // Found first character, now look at the rest of value
        if (i &lt;= max) {
            int j = i + 1;
            int end = j + strCount - 1;
            for (int k = 1; j &lt; end &amp;&amp; value[j] == str[k]; j++, k++);
            if (j == end) {
                // Found whole string.
                return i;
            }
        }
    }
    return -1;
}
</code></pre>
<p>在 HotSpot 虚拟机中，所有被该注解标注的方法都是 HotSpot intrinsic。对这些方法的调用，会被 HotSpot 虚拟机替换成高效的指令序列。而原本的方法实现则会被忽略掉。</p>
<p>换句话说，HotSpot 虚拟机将为标注了<code>@HotSpotIntrinsicCandidate</code>注解的方法额外维护一套高效实现。如果 Java 核心类库的开发者更改了原本的实现，那么虚拟机中的高效实现也需要进行相应的修改，以保证程序语义一致。</p>
<p>需要注意的是，其他虚拟机未必维护了这些 intrinsic 的高效实现，它们可以直接使用原本的较为低效的 JDK 代码。同样，不同版本的 HotSpot 虚拟机所实现的 intrinsic 数量也大不相同。通常越新版本的 Java，其 intrinsic 数量越多。</p>
<p>你或许会产生这么一个疑问：为什么不直接在源代码中使用这些高效实现呢？</p>
<p>这是因为高效实现通常依赖于具体的 CPU 指令，而这些 CPU 指令不好在 Java 源程序中表达。再者，换了一个体系架构，说不定就没有对应的 CPU 指令，也就无法进行 intrinsic 优化了。</p>
<p>下面我们便来看几个具体的例子。</p>
<h2>intrinsic 与 CPU 指令</h2>
<p>在文章开头的例子中，<code>StringLatin1.indexOf</code>方法将在一个字符串（byte 数组）中查找另一个字符串（byte 数组），并且返回命中时的索引值，或者 -1（未命中）。</p>
<p>“恰巧”的是，X86_64 体系架构的 SSE4.2 指令集就包含一条指令 PCMPESTRI，让它能够在 16 字节以下的字符串中，查找另一个 16 字节以下的字符串，并且返回命中时的索引值。</p>
<p>因此，HotSpot 虚拟机便围绕着这一指令，开发出 X86_64 体系架构上的高效实现，并替换原本对<code>StringLatin1.indexOf</code>方法的调用。</p>
<p>另外一个例子则是整数加法的溢出处理。一般我们在做整数加法时，需要考虑结果是否会溢出，并且在溢出的情况下作出相应的处理，以保证程序的正确性。</p>
<p>Java 核心类库提供了一个<code>Math.addExact</code>方法。它将接收两个 int 值（或 long 值）作为参数，并返回这两个 int 值的和。当这两个 int 值之和溢出时，该方法将抛出<code>ArithmeticException</code>异常。</p>
<pre><code>@HotSpotIntrinsicCandidate
public static int addExact(int x, int y) {
    int r = x + y;
    // HD 2-12 Overflow iff both arguments have the opposite sign of the result
    if (((x ^ r) &amp; (y ^ r)) &lt; 0) {
        throw new ArithmeticException(&quot;integer overflow&quot;);
    }
    return r;
}
</code></pre>
<p>在 Java 层面判断 int 值之和是否溢出比较费事。我们需要分别比较两个 int 值与它们的和的符号是否不同。如果都不同，那么我们便认为这两个 int 值之和溢出。对应的实现便是两个异或操作，一个与操作，以及一个比较操作。</p>
<p>在 X86_64 体系架构中，大部分计算指令都会更新状态寄存器（FLAGS register），其中就有表示指令结果是否溢出的溢出标识位（overflow flag）。因此，我们只需在加法指令之后比较溢出标志位，便可以知道 int 值之和是否溢出了。对应的伪代码如下所示：</p>
<pre><code>public static int addExact(int x, int y) {
    int r = x + y;
    jo LABEL_OVERFLOW; // jump if overflow flag set
    return r;
    LABEL_OVERFLOW:
      throw new ArithmeticException(&quot;integer overflow&quot;);
      // or deoptimize
}
</code></pre>
<p>最后一个例子则是<code>Integer.bitCount</code>方法，它将统计所输入的 int 值的二进制形式中有多少个 1。</p>
<pre><code>@HotSpotIntrinsicCandidate
public static int bitCount(int i) {
    // HD, Figure 5-2
    i = i - ((i &gt;&gt;&gt; 1) &amp; 0x55555555);
    i = (i &amp; 0x33333333) + ((i &gt;&gt;&gt; 2) &amp; 0x33333333);
    i = (i + (i &gt;&gt;&gt; 4)) &amp; 0x0f0f0f0f;
    i = i + (i &gt;&gt;&gt; 8);
    i = i + (i &gt;&gt;&gt; 16);
    return i &amp; 0x3f;
}
</code></pre>
<p>我们可以看到，<code>Integer.bitCount</code>方法的实现还是很巧妙的，但是它需要的计算步骤也比较多。在 X86_64 体系架构中，我们仅需要一条指令<code>popcnt</code>，便可以直接统计出 int 值中 1 的个数。</p>
<h2>intrinsic 与方法内联</h2>
<p>HotSpot 虚拟机中，intrinsic 的实现方式分为两种。</p>
<p>一种是独立的桩程序。它既可以被解释执行器利用，直接替换对原方法的调用；也可以被即时编译器所利用，它把代表对原方法的调用的 IR 节点，替换为对这些桩程序的调用的 IR 节点。以这种形式实现的 intrinsic 比较少，主要包括<code>Math</code>类中的一些方法。</p>
<p>另一种则是特殊的编译器 IR 节点。显然，这种实现方式仅能够被即时编译器所利用。</p>
<p>在编译过程中，即时编译器会将对原方法的调用的 IR 节点，替换成特殊的 IR 节点，并参与接下来的优化过程。最终，即时编译器的后端将根据这些特殊的 IR 节点，生成指定的 CPU 指令。大部分的 intrinsic 都是通过这种方式实现的。</p>
<p>这个替换过程是在方法内联时进行的。当即时编译器碰到方法调用节点时，它将查询目标方法是不是 intrinsic。</p>
<p>如果是，则插入相应的特殊 IR 节点；如果不是，则进行原本的内联工作。（即判断是否需要内联目标方法的方法体，并在需要内联的情况下，将目标方法的 IR 图纳入当前的编译范围之中。）</p>
<p>也就是说，如果方法调用的目标方法是 intrinsic，那么即时编译器会直接忽略原目标方法的字节码，甚至根本不在乎原目标方法是否有字节码。即便是 native 方法，只要它被标记为 intrinsic，即时编译器便能够将之 &quot; 内联 &quot; 进来，并插入特殊的 IR 节点。</p>
<p>事实上，不少被标记为 intrinsic 的方法都是 native 方法。原本对这些 native 方法的调用需要经过 JNI（Java Native Interface），其性能开销十分巨大。但是，经过即时编译器的 intrinsic 优化之后，这部分 JNI 开销便直接消失不见，并且最终的结果也十分高效。</p>
<p>举个例子，我们可以通过<code>Thread.currentThread</code>方法来获取当前线程。这是一个 native 方法，同时也是一个 HotSpot intrinsic。在 X86_64 体系架构中，R13 寄存器存放着当前线程的指针。因此，对该方法的调用将被即时编译器替换为一个特殊 IR 节点，并最终生成读取 R13 寄存器指令。</p>
<h2>已有 intrinsic 简介</h2>
<p>最新版本的 HotSpot 虚拟机定义了三百多个 intrinsic。</p>
<p>在这三百多个 intrinsic 中，有三成以上是<code>Unsafe</code>类的方法。不过，我们一般不会直接使用<code>Unsafe</code>类的方法，而是通过<code>java.util.concurrent</code>包来间接使用。</p>
<p>举个例子，<code>Unsafe</code>类中经常会被用到的便是<code>compareAndSwap</code>方法（Java 9+ 更名为<code>compareAndSet</code>或<code>compareAndExchange</code>方法）。在 X86_64 体系架构中，对这些方法的调用将被替换为<code>lock cmpxchg</code>指令，也就是原子性更新指令。</p>
<p>除了<code>Unsafe</code>类的方法之外，HotSpot 虚拟机中的 intrinsic 还包括下面的几种。</p>
<ol>
<li><code>StringBuilder</code>和<code>StringBuffer</code>类的方法。HotSpot 虚拟机将优化利用这些方法构造字符串的方式，以尽量减少需要复制内存的情况。</li>
<li><code>String</code>类、<code>StringLatin1</code>类、<code>StringUTF16</code>类和<code>Arrays</code>类的方法。HotSpot 虚拟机将使用 SIMD 指令（single instruction multiple data，即用一条指令处理多个数据）对这些方法进行优化。
举个例子，<code>Arrays.equals(byte[], byte[])</code>方法原本是逐个字节比较，在使用了 SIMD 指令之后，可以放入 16 字节的 XMM 寄存器中（甚至是 64 字节的 ZMM 寄存器中）批量比较。</li>
<li>基本类型的包装类、<code>Object</code>类、<code>Math</code>类、<code>System</code>类中各个功能性方法，反射 API、<code>MethodHandle</code>类中与调用机制相关的方法，压缩、加密相关方法。这部分 intrinsic 则比较简单，这里就不详细展开了。如果你有感兴趣的，可以自行查阅资料，或者在文末留言。</li>
</ol>
<p>如果你想知道 HotSpot 虚拟机定义的所有 intrinsic，那么你可以直接查阅 OpenJDK 代码 [2]。（该链接是 Java 12 的 intrinsic 列表。Java 8 的 intrinsic 列表可以查阅这一链接 [3]。）</p>
<h2>总结与实践</h2>
<p>今天我介绍了 HotSpot 虚拟机中的 intrinsic。</p>
<p>HotSpot 虚拟机将对标注了<code>@HotSpotIntrinsicCandidate</code>注解的方法的调用，替换为直接使用基于特定 CPU 指令的高效实现。这些方法我们便称之为 intrinsic。</p>
<p>具体来说，intrinsic 的实现有两种。一是不大常见的桩程序，可以在解释执行或者即时编译生成的代码中使用。二是特殊的 IR 节点。即时编译器将在方法内联过程中，将对 intrinsic 的调用替换为这些特殊的 IR 节点，并最终生成指定的 CPU 指令。</p>
<p>HotSpot 虚拟机定义了三百多个 intrinsic。其中比较特殊的有<code>Unsafe</code>类的方法，基本上使用 java.util.concurrent 包便会间接使用到<code>Unsafe</code>类的 intrinsic。除此之外，<code>String</code>类和<code>Arrays</code>类中的 intrinsic 也比较特殊。即时编译器将为之生成非常高效的 SIMD 指令。</p>
<p>今天的实践环节，你可以体验一下<code>Integer.bitCount</code> intrinsic 带来的性能提升。</p>
<pre><code>// time java Foo
public class Foo {
  public static int bitCount(int i) {
    // HD, Figure 5-2
    i = i - ((i &gt;&gt;&gt; 1) &amp; 0x55555555);
    i = (i &amp; 0x33333333) + ((i &gt;&gt;&gt; 2) &amp; 0x33333333);
    i = (i + (i &gt;&gt;&gt; 4)) &amp; 0x0f0f0f0f;
    i = i + (i &gt;&gt;&gt; 8);
    i = i + (i &gt;&gt;&gt; 16);
    return i &amp; 0x3f;
  }
  public static void main(String[] args) {
    int sum = 0;
    for (int i = Integer.MIN_VALUE; i &lt; Integer.MAX_VALUE; i++) {
      sum += bitCount(i); // In a second run, replace with Integer.bitCount
    }
    System.out.println(sum);
  }
}
</code></pre>
<p>[1] <a href="https://openjdk.java.net/jeps/254">http://openjdk.java.net/jeps/254</a>
[2] <a href="http://hg.openjdk.java.net/jdk/hs/file/46dc568d6804/src/hotspot/share/classfile/vmSymbols.hpp#l727">http://hg.openjdk.java.net/jdk/hs/file/46dc568d6804/src/hotspot/share/classfile/vmSymbols.hpp#l727</a>
[3] <a href="http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/2af8917ffbee/src/share/vm/classfile/vmSymbols.hpp#l647">http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/2af8917ffbee/src/share/vm/classfile/vmSymbols.hpp#l647</a></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="21&#32;&#32;方法内联（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="23&#32;&#32;逃逸分析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4357df4f2a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
