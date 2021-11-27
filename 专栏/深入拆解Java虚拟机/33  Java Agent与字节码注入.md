<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>33  Java Agent与字节码注入.md</title>
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

                    <a class="current-tab" href="33&#32;&#32;Java&#32;Agent与字节码注入.md">33  Java Agent与字节码注入.md</a>
                    

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
                        <div><h1>33  Java Agent与字节码注入</h1>
<p>关于 Java agent，大家可能都听过大名鼎鼎的<code>premain</code>方法。顾名思义，这个方法指的就是在<code>main</code>方法之前执行的方法。</p>
<pre><code>package org.example;
 
public class MyAgent {
  public static void premain(String args) {
    System.out.println(&quot;premain&quot;);
  }
}
</code></pre>
<p>我在上面这段代码中定义了一个<code>premain</code>方法。这里需要注意的是，Java 虚拟机所能识别的<code>premain</code>方法接收的是字符串类型的参数，而并非类似于<code>main</code>方法的字符串数组。</p>
<p>为了能够以 Java agent 的方式运行该<code>premain</code>方法，我们需要将其打包成 jar 包，并在其中的 MANIFEST.MF 配置文件中，指定所谓的<code>Premain-class</code>。具体的命令如下所示：</p>
<pre><code># 注意第一条命令会向 manifest.txt 文件写入两行数据，其中包括一行空行
$ echo 'Premain-Class: org.example.MyAgent
' &gt; manifest.txt
$ jar cvmf manifest.txt myagent.jar org/
$ java -javaagent:myagent.jar HelloWorld
premain
Hello, World
</code></pre>
<p>除了在命令行中指定 Java agent 之外，我们还可以通过 Attach API 远程加载。具体用法如下面的代码所示：</p>
<pre><code>import java.io.IOException;
 
import com.sun.tools.attach.*;
 
public class AttachTest {
  public static void main(String[] args)
      throws AttachNotSupportedException, IOException, AgentLoadException, AgentInitializationException {
    if (args.length &lt;= 1) {
      System.out.println(&quot;Usage: java AttachTest &lt;PID&gt; /PATH/TO/AGENT.jar&quot;);
      return;
    }
    VirtualMachine vm = VirtualMachine.attach(args[0]);
    vm.loadAgent(args[1]);
  }
}
 
</code></pre>
<p>使用 Attach API 远程加载的 Java agent 不会再先于<code>main</code>方法执行，这取决于另一虚拟机调用 Attach API 的时机。并且，它运行的也不再是<code>premain</code>方法，而是名为<code>agentmain</code>的方法。</p>
<pre><code>public class MyAgent { 
  public static void agentmain(String args) {
    System.out.println(&quot;agentmain&quot;);
  }
}
</code></pre>
<p>相应的，我们需要更新 jar 包中的 manifest 文件，使其包含<code>Agent-Class</code>的配置，例如<code>Agent-Class: org.example.MyAgent</code>。</p>
<pre><code>$ echo 'Agent-Class: org.example.MyAgent
' &gt; manifest.txt
$ jar cvmf manifest.txt myagent.jar org/
$ java HelloWorld
Hello, World
$ jps
$ java AttachTest &lt;pid&gt; myagent.jar
agentmain
// 最后一句输出来自于运行 HelloWorld 的 Java 进程
</code></pre>
<p>Java 虚拟机并不限制 Java agent 的数量。你可以在 java 命令后附上多个<code>-javaagent</code>参数，或者远程 attach 多个 Java agent，Java 虚拟机会按照定义顺序，或者 attach 的顺序逐个执行这些 Java agent。</p>
<p>在<code>premain</code>方法或者<code>agentmain</code>方法中打印一些字符串并不出奇，我们完全可以将其中的逻辑并入<code>main</code>方法，或者其他监听端口的线程中。除此之外，Java agent 还提供了一套 instrumentation 机制，允许应用程序拦截类加载事件，并且更改该类的字节码。</p>
<p>接下来，我们来了解一下基于这一机制的字节码注入。</p>
<h2>字节码注入</h2>
<pre><code>package org.example;
 
import java.lang.instrument.*;
import java.security.ProtectionDomain;
 
public class MyAgent {
  public static void premain(String args, Instrumentation instrumentation) {
    instrumentation.addTransformer(new MyTransformer());
  }
 
  static class MyTransformer implements ClassFileTransformer {
    public byte[] transform(ClassLoader loader, String className, Class&lt;?&gt; classBeingRedefined,
        ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException {
      System.out.printf(&quot;Loaded %s: 0x%X%X%X%X\n&quot;, className, classfileBuffer[0], classfileBuffer[1],
          classfileBuffer[2], classfileBuffer[3]);
      return null;
    }
  }
}
</code></pre>
<p>我们先来看一个例子。在上面这段代码中，<code>premain</code>方法多出了一个<code>Instrumentation</code>类型的参数，我们可以通过它来注册类加载事件的拦截器。该拦截器需要实现<code>ClassFileTransformer</code>接口，并重写其中的<code>transform</code>方法。</p>
<p><code>transform</code>方法将接收一个 byte 数组类型的参数，它代表的是正在被加载的类的字节码。在上面这段代码中，我将打印该数组的前四个字节，也就是 Java class 文件的魔数（magic number）0xCAFEBABE。</p>
<p><code>transform</code>方法将返回一个 byte 数组，代表更新过后的类的字节码。当方法返回之后，Java 虚拟机会使用所返回的 byte 数组，来完成接下来的类加载工作。不过，如果<code>transform</code>方法返回 null 或者抛出异常，那么 Java 虚拟机将使用原来的 byte 数组完成类加载工作。</p>
<p>基于这一类加载事件的拦截功能，我们可以实现字节码注入（bytecode instrumentation），往正在被加载的类中插入额外的字节码。</p>
<p>在工具篇中我曾经介绍过字节码工程框架 ASM 的用法。下面我将演示它的<a href="https://search.maven.org/artifact/org.ow2.asm/asm-tree/7.0-beta/jar">tree 包</a>（依赖于<a href="https://search.maven.org/artifact/org.ow2.asm/asm/7.0-beta/jar">基础包</a>），用面向对象的方式注入字节码。</p>
<pre><code>package org.example;
 
import java.lang.instrument.*;
import java.security.ProtectionDomain;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;
 
public class MyAgent {
  public static void premain(String args, Instrumentation instrumentation) {
    instrumentation.addTransformer(new MyTransformer());
  }
 
  static class MyTransformer implements ClassFileTransformer, Opcodes {
    public byte[] transform(ClassLoader loader, String className, Class&lt;?&gt; classBeingRedefined,
        ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException {
      ClassReader cr = new ClassReader(classfileBuffer);
      ClassNode classNode = new ClassNode(ASM7);
      cr.accept(classNode, ClassReader.SKIP_FRAMES);
 
      for (MethodNode methodNode : classNode.methods) {
        if (&quot;main&quot;.equals(methodNode.name)) {
          InsnList instrumentation = new InsnList();
          instrumentation.add(new FieldInsnNode(GETSTATIC, &quot;java/lang/System&quot;, &quot;out&quot;, &quot;Ljava/io/PrintStream;&quot;));
          instrumentation.add(new LdcInsnNode(&quot;Hello, Instrumentation!&quot;));
          instrumentation
              .add(new MethodInsnNode(INVOKEVIRTUAL, &quot;java/io/PrintStream&quot;, &quot;println&quot;, &quot;(Ljava/lang/String;)V&quot;, false));
 
          methodNode.instructions.insert(instrumentation);
        }
      }
 
      ClassWriter cw = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS);
      classNode.accept(cw);
      return cw.toByteArray();
    }
  }
}
</code></pre>
<p>上面这段代码不难理解。我们将使用<code>ClassReader</code>读取所传入的 byte 数组，并将其转换成<code>ClassNode</code>。然后我们将遍历<code>ClassNode</code>中的<code>MethodNode</code>节点，也就是该类中的构造器和方法。</p>
<p>当遇到名字为<code>&quot;main&quot;</code>的方法时，我们会在方法的入口处注入<code>System.out.println(&quot;Hello, Instrumentation!&quot;);</code>。运行结果如下所示：</p>
<pre><code>$ java -javaagent:myagent.jar -cp .:/PATH/TO/asm-7.0-beta.jar:/PATH/TO/asm-tree-7.0-beta.jar HelloWorld
Hello, Instrumentation!
Hello, World!
</code></pre>
<p>Java agent 还提供了另外两个功能<code>redefine</code>和<code>retransform</code>。这两个功能针对的是已加载的类，并要求用户传入所要<code>redefine</code>或者<code>retransform</code>的类实例。</p>
<p>其中，<code>redefine</code>指的是舍弃原本的字节码，并替换成由用户提供的 byte 数组。该功能比较危险，一般用于修复出错了的字节码。</p>
<p><code>retransform</code>则将针对所传入的类，重新调用所有已注册的<code>ClassFileTransformer</code>的<code>transform</code>方法。它的应用场景主要有如下两个。</p>
<p>第一，在执行<code>premain</code>或者<code>agentmain</code>方法前，Java 虚拟机早已加载了不少类，而这些类的加载事件并没有被拦截，因此也没有被注入。使用<code>retransform</code>功能可以注入这些已加载但未注入的类。</p>
<p>第二，在定义了多个 Java agent，多个注入的情况下，我们可能需要移除其中的部分注入。当调用<code>Instrumentation.removeTransformer</code>去除某个注入类后，我们可以调用<code>retransform</code>功能，重新从原始 byte 数组开始进行注入。</p>
<p>Java agent 的这些功能都是通过 JVMTI agent，也就是 C agent 来实现的。JVMTI 是一个事件驱动的工具实现接口，通常，我们会在 C agent 加载后的入口方法<code>Agent_OnLoad</code>处注册各个事件的钩子（hook）方法。当 Java 虚拟机触发了这些事件时，便会调用对应的钩子方法。</p>
<pre><code>JNIEXPORT jint JNICALL
Agent_OnLoad(JavaVM *vm, char *options, void *reserved);
</code></pre>
<p>举个例子，我们可以为 JVMTI 中的<code>ClassFileLoadHook</code>事件设置钩子，从而在 C 层面拦截所有的类加载事件。关于 JVMTI 的其他事件，你可以参考该<a href="https://docs.oracle.com/en/java/javase/11/docs/specs/jvmti.html#EventIndex">链接</a>。</p>
<h2>基于字节码注入的 profiler</h2>
<p>我们可以利用字节码注入来实现代码覆盖工具（例如<a href="https://www.jacoco.org/jacoco/">JaCoCo</a>），或者各式各样的 profiler。</p>
<p>通常，我们会定义一个运行时类，并在某一程序行为的周围，注入对该运行时类中方法的调用，以表示该程序行为正要发生或者已经发生。</p>
<pre><code>package org.example;
 
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;
 
public class MyProfiler {
  public static ConcurrentHashMap&lt;Class&lt;?&gt;, AtomicInteger&gt; data = new ConcurrentHashMap&lt;&gt;();
 
  public static void fireAllocationEvent(Class&lt;?&gt; klass) {
    data.computeIfAbsent(klass, kls -&gt; new AtomicInteger())
        .incrementAndGet();
  }
 
  public static void dump() {
    data.forEach((kls, counter) -&gt; {
      System.err.printf(&quot;%s: %d\n&quot;, kls.getName(), counter.get());
    });
  }
 
  static {
    Runtime.getRuntime().addShutdownHook(new Thread(MyProfiler::dump));
  }
}
</code></pre>
<p>举个例子，上面这段代码便是一个运行时类。该类维护了一个<code>HashMap</code>，用来统计每个类所新建实例的数目。当程序退出时，我们将逐个打印出每个类的名字，以及其新建实例的数目。</p>
<p>在 Java agent 中，我们会截获正在加载的类，并且在每条<code>new</code>字节码之后插入对<code>fireAllocationEvent</code>方法的调用，以表示当前正在新建某个类的实例。具体的注入代码如下所示：</p>
<pre><code>package org.example;
 
import java.lang.instrument.*;
import java.security.ProtectionDomain;
 
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;
 
public class MyAgent {
 
  public static void premain(String args, Instrumentation instrumentation) {
    instrumentation.addTransformer(new MyTransformer());
  }
 
  static class MyTransformer implements ClassFileTransformer, Opcodes {
    public byte[] transform(ClassLoader loader, String className, Class&lt;?&gt; classBeingRedefined,
        ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException {
      if (className.startsWith(&quot;java&quot;)    ||
          className.startsWith(&quot;javax&quot;)   || 
          className.startsWith(&quot;jdk&quot;)     ||
          className.startsWith(&quot;sun&quot;)     ||
          className.startsWith(&quot;com/sun&quot;) ||
          className.startsWith(&quot;org/example&quot;)) {
        // Skip JDK classes and profiler classes
        return null;
      }
 
      ClassReader cr = new ClassReader(classfileBuffer);
      ClassNode classNode = new ClassNode(ASM7);
      cr.accept(classNode, ClassReader.SKIP_FRAMES);
 
      for (MethodNode methodNode : classNode.methods) {
        for (AbstractInsnNode node : methodNode.instructions.toArray()) {
          if (node.getOpcode() == NEW) {
            TypeInsnNode typeInsnNode = (TypeInsnNode) node;
 
            InsnList instrumentation = new InsnList();
            instrumentation.add(new LdcInsnNode(Type.getObjectType(typeInsnNode.desc)));
            instrumentation.add(new MethodInsnNode(INVOKESTATIC, &quot;org/example/MyProfiler&quot;, &quot;fireAllocationEvent&quot;,
                &quot;(Ljava/lang/Class;)V&quot;, false));
 
            methodNode.instructions.insert(node, instrumentation);
          }
        }
      }
 
      ClassWriter cw = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS);
      classNode.accept(cw);
      return cw.toByteArray();
    }
  }
 
}
</code></pre>
<p>你或许已经留意到，我们不得不排除对 JDK 类以及该运行时类的注入。这是因为，对这些类的注入很可能造成死循环调用，并最终抛出<code>StackOverflowException</code>异常。</p>
<p>举个例子，假设我们在<code>PrintStream.println</code>方法入口处注入<code>System.out.println(&quot;blahblah&quot;)</code>，由于<code>out</code>是<code>PrintStream</code>的实例，因此当执行注入代码时，我们又会调用<code>PrintStream.println</code>方法，从而造成死循环。</p>
<p>解决这一问题的关键在于设置一个线程私有的标识位，用以区分应用代码的上下文以及注入代码的上下文。当即将执行注入代码时，我们将根据标识位判断是否已经位于注入代码的上下文之中。如果不是，则设置标识位并正常执行注入代码；如果是，则直接返回，不再执行注入代码。</p>
<p>字节码注入的另一个技术难点则是命名空间。举个例子，不少应用程序都依赖于字节码工程库 ASM。当我们的注入逻辑依赖于 ASM 时，便有可能出现注入使用最新版本的 ASM，而应用程序使用较低版本的 ASM 的问题。</p>
<p>JDK 本身也使用了 ASM 库，如用来生成 Lambda 表达式的适配器类。JDK 的做法是重命名整个 ASM 库，为所有类的包名添加<code>jdk.internal</code>前缀。我们显然不好直接更改 ASM 的包名，因此需要借助自定义类加载器来隔离命名空间。</p>
<p>除了上述技术难点之外，基于字节码注入的工具还有另一个问题，那便是观察者效应（observer effect）对所收集的数据造成的影响。</p>
<p>举个利用字节码注入收集每个方法的运行时间的例子。假设某个方法调用了另一个方法，而这两个方法都被注入了，那么统计被调用者运行时间的注入代码所耗费的时间，将不可避免地被计入至调用者方法的运行时间之中。</p>
<p>再举一个统计新建对象数目的例子。我们知道，即时编译器中的逃逸分析可能会优化掉新建对象操作，但它不会消除相应的统计操作，比如上述例子中对<code>fireAllocationEvent</code>方法的调用。在这种情况下，我们将统计没有实际发生的新建对象操作。</p>
<p>另一种情况则是，我们所注入的对<code>fireAllocationEvent</code>方法的调用，将影响到方法内联的决策。如果该新建对象的构造器调用恰好因此没有被内联，从而造成对象逃逸。在这种情况下，原本能够被逃逸分析优化掉的新建对象操作将无法优化，我们也将统计到原本不会发生的新建对象操作。</p>
<p>总而言之，当使用字节码注入开发 profiler 时，需要辩证地看待所收集的数据。它仅能表示在被注入的情况下程序的执行状态，而非没有注入情况下的程序执行状态。</p>
<h2>面向方面编程</h2>
<p>说到字节码注入，就不得不提面向方面编程（Aspect-Oriented Programming，AOP）。面向方面编程的核心理念是定义切入点（pointcut）以及通知（advice）。程序控制流中所有匹配该切入点的连接点（joinpoint）都将执行这段通知代码。</p>
<p>举个例子，我们定义一个指代所有方法入口的切入点，并指定在该切入点执行的“打印该方法的名字”这一通知。那么每个具体的方法入口便是一个连接点。</p>
<p>面向方面编程的其中一种实现方式便是字节码注入，比如<a href="https://www.eclipse.org/aspectj/">AspectJ</a>。</p>
<p>在前面的例子中，我们也相当于使用了面向方面编程，在所有的<code>new</code>字节码之后执行了下面这样一段通知代码。</p>
<pre><code>`MyProfiler.fireAllocationEvent(&lt;Target&gt;.class)`
</code></pre>
<p>我曾经参与开发过一个应用了面向方面编程思想的字节码注入框架<a href="https://disl.ow2.org/">DiSL</a>。它支持用注解来定义切入点，用普通 Java 方法来定义通知。例如，在方法入口处打印所在的方法名，可以简单表示为如下代码：</p>
<pre><code>@Before(marker = BodyMarker.class)
static void onMethodEntry(MethodStaticContext msc) {
  System.out.println(msc.thisMethodFullName());
}
</code></pre>
<p>如果有同学对这个工具感兴趣，或者有什么需求或者建议，欢迎你在留言中提出。</p>
<h2>总结与实践</h2>
<p>今天我介绍了 Java agent 以及字节码注入。</p>
<p>我们可以通过 Java agent 的类加载拦截功能，修改某个类所对应的 byte 数组，并利用这个修改过后的 byte 数组完成接下来的类加载。</p>
<p>基于字节码注入的 profiler，可以统计程序运行过程中某些行为的出现次数。如果需要收集 Java 核心类库的数据，那么我们需要小心避免无限递归调用。另外，我们还需通过自定义类加载器来解决命名空间的问题。</p>
<p>由于字节码注入会产生观察者效应，因此基于该技术的 profiler 所收集到的数据并不能反映程序的真实运行状态。它所反映的是程序在被注入的情况下的执行状态。</p>
<hr />
<p>今天的实践环节，请你思考如何注入方法出口。除了正常执行路径之外，你还需考虑异常执行路径。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="32&#32;&#32;JNI的运行机制.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="34&#32;&#32;Graal：用Java编译Java.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43582a4949645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
