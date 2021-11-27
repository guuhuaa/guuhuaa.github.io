<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>32  JNI的运行机制.md</title>
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

                    <a class="current-tab" href="32&#32;&#32;JNI的运行机制.md">32  JNI的运行机制.md</a>
                    

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
                        <div><h1>32  JNI的运行机制</h1>
<p>我们经常会遇见 Java 语言较难表达，甚至是无法表达的应用场景。比如我们希望使用汇编语言（如 X86_64 的 SIMD 指令）来提升关键代码的性能；再比如，我们希望调用 Java 核心类库无法提供的，某个体系架构或者操作系统特有的功能。</p>
<p>在这种情况下，我们往往会牺牲可移植性，在 Java 代码中调用 C/C++ 代码（下面简述为 C 代码），并在其中实现所需功能。这种跨语言的调用，便需要借助 Java 虚拟机的 Java Native Interface（JNI）机制。</p>
<p>关于 JNI 的例子，你应该特别熟悉 Java 中标记为<code>native</code>的、没有方法体的方法（下面统称为 native 方法）。当在 Java 代码中调用这些 native 方法时，Java 虚拟机将通过 JNI，调用至对应的 C 函数（下面将 native 方法对应的 C 实现统称为 C 函数）中。</p>
<pre><code>public class Object {
  public native int hashCode();
}
</code></pre>
<p>举个例子，<code>Object.hashCode</code>方法便是一个 native 方法。它对应的 C 函数将计算对象的哈希值，并缓存在对象头、栈上锁记录（轻型锁）或对象监视锁（重型锁所使用的 monitor）中，以确保该值在对象的生命周期之内不会变更。</p>
<h2>native 方法的链接</h2>
<p>在调用 native 方法前，Java 虚拟机需要将该 native 方法链接至对应的 C 函数上。</p>
<p>链接方式主要有两种。第一种是让 Java 虚拟机自动查找符合默认命名规范的 C 函数，并且链接起来。</p>
<p>事实上，我们并不需要记住所谓的命名规范，而是采用<code>javac -h</code>命令，便可以根据 Java 程序中的 native 方法声明，自动生成包含符合命名规范的 C 函数的头文件。</p>
<p>举个例子，在下面这段代码中，<code>Foo</code>类有三个 native 方法，分别为静态方法<code>foo</code>以及两个重载的实例方法<code>bar</code>。</p>
<pre><code>package org.example;
 
public class Foo {
  public static native void foo();
  public native void bar(int i, long j);
  public native void bar(String s, Object o);
}
</code></pre>
<p>通过执行<code>javac -h . org/example/Foo.java</code>命令，我们将在当前文件夹（对应<code>-h</code>后面跟着的<code>.</code>）生成名为<code>org_example_Foo.h</code>的头文件。其内容如下所示：</p>
<pre><code>/* DO NOT EDIT THIS FILE - it is machine generated */
#include &lt;jni.h&gt;
/* Header for class org_example_Foo */
 
#ifndef _Included_org_example_Foo
#define _Included_org_example_Foo
#ifdef __cplusplus
extern &quot;C&quot; {
#endif
/*
 * Class:     org_example_Foo
 * Method:    foo
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_org_example_Foo_foo
  (JNIEnv *, jclass);
 
/*
 * Class:     org_example_Foo
 * Method:    bar
 * Signature: (IJ)V
 */
JNIEXPORT void JNICALL Java_org_example_Foo_bar__IJ
  (JNIEnv *, jobject, jint, jlong);
 
/*
 * Class:     org_example_Foo
 * Method:    bar
 * Signature: (Ljava/lang/String;Ljava/lang/Object;)V
 */
JNIEXPORT void JNICALL Java_org_example_Foo_bar__Ljava_lang_String_2Ljava_lang_Object_2
  (JNIEnv *, jobject, jstring, jobject);
 
#ifdef __cplusplus
}
#endif
#endif
</code></pre>
<p>这里我简单讲解一下该命名规范。</p>
<p>首先，native 方法对应的 C 函数都需要以<code>Java_</code>为前缀，之后跟着完整的包名和方法名。由于 C 函数名不支持<code>/</code>字符，因此我们需要将<code>/</code>转换为<code>_</code>，而原本方法名中的<code>_</code>符号，则需要转换为<code>_1</code>。</p>
<p>举个例子，<code>org.example</code>包下<code>Foo</code>类的<code>foo</code>方法，Java 虚拟机会将其自动链接至名为<code>Java_org_example_Foo_foo</code>的 C 函数中。</p>
<p>当某个类出现重载的 native 方法时，Java 虚拟机还会将参数类型纳入自动链接对象的考虑范围之中。具体的做法便是在前面 C 函数名的基础上，追加<code>__</code>以及方法描述符作为后缀。</p>
<p>方法描述符的特殊符号同样会被替换掉，如引用类型所使用的<code>;</code>会被替换为<code>_2</code>，数组类型所使用的<code>[</code>会被替换为<code>_3</code>。</p>
<p>基于此命名规范，你可以手动拼凑上述代码中，<code>Foo</code>类的两个<code>bar</code>方法所能自动链接的 C 函数名，并用<code>javac -h</code>命令所生成的结果来验证一下。</p>
<p>第二种链接方式则是在 C 代码中主动链接。</p>
<p>这种链接方式对 C 函数名没有要求。通常我们会使用一个名为<code>registerNatives</code>的 native 方法，并按照第一种链接方式定义所能自动链接的 C 函数。在该 C 函数中，我们将手动链接该类的其他 native 方法。</p>
<p>举个例子，<code>Object</code>类便拥有一个<code>registerNatives</code>方法，所对应的 C 代码如下所示：</p>
<pre><code>// 注：Object 类的 registerNatives 方法的实现位于 java.base 模块里的 C 代码中
static JNINativeMethod methods[] = {
    {&quot;hashCode&quot;,    &quot;()I&quot;,                    (void *)&amp;JVM_IHashCode},
    {&quot;wait&quot;,        &quot;(J)V&quot;,                   (void *)&amp;JVM_MonitorWait},
    {&quot;notify&quot;,      &quot;()V&quot;,                    (void *)&amp;JVM_MonitorNotify},
    {&quot;notifyAll&quot;,   &quot;()V&quot;,                    (void *)&amp;JVM_MonitorNotifyAll},
    {&quot;clone&quot;,       &quot;()Ljava/lang/Object;&quot;,   (void *)&amp;JVM_Clone},
};
 
JNIEXPORT void JNICALL
Java_java_lang_Object_registerNatives(JNIEnv *env, jclass cls)
{
    (*env)-&gt;RegisterNatives(env, cls,
                            methods, sizeof(methods)/sizeof(methods[0]));
}
</code></pre>
<p>我们可以看到，上面这段代码中的 C 函数将调用<code>RegisterNatives</code> API，注册<code>Object</code>类中其他 native 方法所要链接的 C 函数。并且，这些 C 函数的名字并不符合默认命名规则。</p>
<p>当使用第二种方式进行链接时，我们需要在其他 native 方法被调用之前完成链接工作。因此，我们往往会在类的初始化方法里调用该<code>registerNatives</code>方法。具体示例如下所示：</p>
<pre><code>public class Object {
    private static native void registerNatives();
    static {
        registerNatives();
    }
}
</code></pre>
<p>下面我们采用第一种链接方式，并且实现其中的<code>bar(String, Object)</code>方法。如下所示：</p>
<pre><code>// foo.c
#include &lt;stdio.h&gt;
#include &quot;org_example_Foo.h&quot;
 
JNIEXPORT void JNICALL Java_org_example_Foo_bar__Ljava_lang_String_2Ljava_lang_Object_2
  (JNIEnv *env, jobject thisObject, jstring str, jobject obj) {
  printf(&quot;Hello, World\n&quot;);
  return;
}
</code></pre>
<p>然后，我们可以通过 gcc 命令将其编译成为动态链接库：</p>
<pre><code># 该命令仅适用于 macOS
$ gcc -I$JAVA_HOME/include -I$JAVA_HOME/include/darwin -o libfoo.dylib -shared foo.c
</code></pre>
<p>这里需要注意的是，动态链接库的名字须以<code>lib</code>为前缀，以<code>.dylib</code>(或 Linux 上的<code>.so</code>）为扩展名。在 Java 程序中，我们可以通过<code>System.loadLibrary(&quot;foo&quot;)</code>方法来加载<code>libfoo.dylib</code>，如下述代码所示：</p>
<pre><code>package org.example;
 
public class Foo {
  public static native void foo();
  public native void bar(int i, long j);
  public native void bar(String s, Object o);
 
  int i = 0xDEADBEEF;
 
  public static void main(String[] args) {
    try {
      System.loadLibrary(&quot;foo&quot;);
    } catch (UnsatisfiedLinkError e) {
      e.printStackTrace();
      System.exit(1);
    }
    new Foo().bar(&quot;&quot;, &quot;&quot;);
  }
}
</code></pre>
<p>如果<code>libfoo.dylib</code>不在当前路径下，我们可以在启动 Java 虚拟机时配置<code>java.library.path</code>参数，使其指向包含<code>libfoo.dylib</code>的文件夹。具体命令如下所示：</p>
<pre><code>$ java -Djava.library.path=/PATH/TO/DIR/CONTAINING/libfoo.dylib org.example.Foo
Hello, World
</code></pre>
<h2>JNI 的 API</h2>
<p>在 C 代码中，我们也可以使用 Java 的语言特性，如 instanceof 测试等。这些功能都是通过特殊的 JNI 函数（<a href="https://docs.oracle.com/en/java/javase/11/docs/specs/jni/functions.html">JNI Functions</a>）来实现的。</p>
<p>Java 虚拟机会将所有 JNI 函数的函数指针聚合到一个名为<code>JNIEnv</code>的数据结构之中。</p>
<p>这是一个线程私有的数据结构。Java 虚拟机会为每个线程创建一个<code>JNIEnv</code>，并规定 C 代码不能将当前线程的<code>JNIEnv</code>共享给其他线程，否则 JNI 函数的正确性将无法保证。</p>
<p>这么设计的原因主要有两个。一是给 JNI 函数提供一个单独命名空间。二是允许 Java 虚拟机通过更改函数指针替换 JNI 函数的具体实现，例如从附带参数类型检测的慢速版本，切换至不做参数类型检测的快速版本。</p>
<p>在 HotSpot 虚拟机中，<code>JNIEnv</code>被内嵌至 Java 线程的数据结构之中。部分虚拟机代码甚至会从<code>JNIEnv</code>的地址倒推出 Java 线程的地址。因此，如果在其他线程中使用当前线程的<code>JNIEnv</code>，会使这部分代码错误识别当前线程。</p>
<p>JNI 会将 Java 层面的基本类型以及引用类型映射为另一套可供 C 代码使用的数据结构。其中，基本类型的对应关系如下表所示：</p>
<p><img src="assets/cb2c806532449f2c1edfe821990ac9ca.png" alt="img" /></p>
<p>引用类型对应的数据结构之间也存在着继承关系，具体如下所示：</p>
<pre><code>jobject
|- jclass (java.lang.Class objects)
|- jstring (java.lang.String objects)
|- jthrowable (java.lang.Throwable objects)
|- jarray (arrays)
   |- jobjectArray (object arrays)
   |- jbooleanArray (boolean arrays)
   |- jbyteArray (byte arrays)
   |- jcharArray (char arrays)
   |- jshortArray (short arrays)
   |- jintArray (int arrays)
   |- jlongArray (long arrays)
   |- jfloatArray (float arrays)
   |- jdoubleArray (double arrays)
</code></pre>
<p>我们回头看看<code>Foo</code>类 3 个 native 方法对应的 C 函数的参数。</p>
<pre><code>JNIEXPORT void JNICALL Java_org_example_Foo_foo
  (JNIEnv *, jclass);
 
JNIEXPORT void JNICALL Java_org_example_Foo_bar__IJ
  (JNIEnv *, jobject, jint, jlong);
 
JNIEXPORT void JNICALL Java_org_example_Foo_bar__Ljava_lang_String_2Ljava_lang_Object_2  (JNIEnv *, jobject, jstring, jobject);
</code></pre>
<p>静态 native 方法<code>foo</code>将接收两个参数，分别为存放 JNI 函数的<code>JNIEnv</code>指针，以及一个<code>jclass</code>参数，用来指代定义该 native 方法的类，即<code>Foo</code>类。</p>
<p>两个实例 native 方法<code>bar</code>的第二个参数则是<code>jobject</code>类型的，用来指代该 native 方法的调用者，也就是<code>Foo</code>类的实例。</p>
<p>如果 native 方法声明了参数，那么对应的 C 函数将接收这些参数。在我们的例子中，第一个<code>bar</code>方法声明了 int 型和 long 型的参数，对应的 C 函数则接收 jint 和 jlong 类型的参数；第二个<code>bar</code>方法声明了 String 类型和 Object 类型的参数，对应的 C 函数则接收 jstring 和 jobject 类型的参数。</p>
<p>下面，我们继续修改上一小节中的<code>foo.c</code>，并在 C 代码中获取<code>Foo</code>类实例的<code>i</code>字段。</p>
<pre><code>// foo.c
#include &lt;stdio.h&gt;
#include &quot;org_example_Foo.h&quot;
 
JNIEXPORT void JNICALL Java_org_example_Foo_bar__Ljava_lang_String_2Ljava_lang_Object_2
  (JNIEnv *env, jobject thisObject, jstring str, jobject obj) {
  jclass cls = (*env)-&gt;GetObjectClass(env, thisObject);
  jfieldID fieldID = (*env)-&gt;GetFieldID(env, cls, &quot;i&quot;, &quot;I&quot;);
  jint value = (*env)-&gt;GetIntField(env, thisObject, fieldID);
  printf(&quot;Hello, World 0x%x\n&quot;, value);
  return;
}
</code></pre>
<p>我们可以看到，在 JNI 中访问字段类似于反射 API：我们首先需要通过类实例获得<code>FieldID</code>，然后再通过<code>FieldID</code>获得某个实例中该字段的值。不过，与 Java 代码相比，上述代码貌似不用处理异常。事实果真如此吗？</p>
<p>下面我就尝试获取了不存在的字段<code>j</code>，运行结果如下所示：</p>
<pre><code>$ java org.example.Foo
Hello, World 0x5
Exception in thread &quot;main&quot; java.lang.NoSuchFieldError: j
 at org.example.Foo.bar(Native Method)
 at org.example.Foo.main(Foo.java:20)
</code></pre>
<p>我们可以看到，<code>printf</code>语句照常执行并打印出<code>Hello, World 0x5</code>，但这个数值明显是错误的。当从 C 函数返回至 main 方法时，Java 虚拟机又会抛出<code>NoSuchFieldError</code>异常。</p>
<p>实际上，当调用 JNI 函数时，Java 虚拟机便已生成异常实例，并缓存在内存中的某个位置。与 Java 编程不一样的是，它并不会显式地跳转至异常处理器或者调用者中，而是继续执行接下来的 C 代码。</p>
<p>因此，当从可能触发异常的 JNI 函数返回时，我们需要通过 JNI 函数<code>ExceptionOccurred</code>检查是否发生了异常，并且作出相应的处理。如果无须抛出该异常，那么我们需要通过 JNI 函数<code>ExceptionClear</code>显式地清空已缓存的异常。</p>
<p>具体示例如下所示（为了控制代码篇幅，我仅在第一个<code>GetFieldID</code>后检查异常以及清空异常）：</p>
<pre><code>// foo.c
#include &lt;stdio.h&gt;
#include &quot;org_example_Foo.h&quot;
 
JNIEXPORT void JNICALL Java_org_example_Foo_bar__Ljava_lang_String_2Ljava_lang_Object_2
  (JNIEnv *env, jobject thisObject, jstring str, jobject obj) {
  jclass cls = (*env)-&gt;GetObjectClass(env, thisObject);
  jfieldID fieldID = (*env)-&gt;GetFieldID(env, cls, &quot;j&quot;, &quot;I&quot;);
  if((*env)-&gt;ExceptionOccurred(env)) {
    printf(&quot;Exception!\n&quot;);
    (*env)-&gt;ExceptionClear(env);
  }
  fieldID = (*env)-&gt;GetFieldID(env, cls, &quot;i&quot;, &quot;I&quot;);
  jint value = (*env)-&gt;GetIntField(env, thisObject, fieldID);
  // we should put an exception guard here as well.
  printf(&quot;Hello, World 0x%x\n&quot;, value);
  return;
}
</code></pre>
<h2>局部引用与全局引用</h2>
<p>在 C 代码中，我们可以访问所传入的引用类型参数，也可以通过 JNI 函数创建新的 Java 对象。</p>
<p>这些 Java 对象显然也会受到垃圾回收器的影响。因此，Java 虚拟机需要一种机制，来告知垃圾回收算法，不要回收这些 C 代码中可能引用到的 Java 对象。</p>
<p>这种机制便是 JNI 的局部引用（Local Reference）和全局引用（Global Reference）。垃圾回收算法会将被这两种引用指向的对象标记为不可回收。</p>
<p>事实上，无论是传入的引用类型参数，还是通过 JNI 函数（除<code>NewGlobalRef</code>及<code>NewWeakGlobalRef</code>之外）返回的引用类型对象，都属于局部引用。</p>
<p>不过，一旦从 C 函数中返回至 Java 方法之中，那么局部引用将失效。也就是说，垃圾回收器在标记垃圾时不再考虑这些局部引用。</p>
<p>这就意味着，我们不能缓存局部引用，以供另一 C 线程或下一次 native 方法调用时使用。</p>
<p>对于这种应用场景，我们需要借助 JNI 函数<code>NewGlobalRef</code>，将该局部引用转换为全局引用，以确保其指向的 Java 对象不会被垃圾回收。</p>
<p>相应的，我们还可以通过 JNI 函数<code>DeleteGlobalRef</code>来消除全局引用，以便回收被全局引用指向的 Java 对象。</p>
<p>此外，当 C 函数运行时间极其长时，我们也应该考虑通过 JNI 函数<code>DeleteLocalRef</code>，消除不再使用的局部引用，以便回收被引用的 Java 对象。</p>
<p>另一方面，由于垃圾回收器可能会移动对象在内存中的位置，因此 Java 虚拟机需要另一种机制，来保证局部引用或者全局引用将正确地指向移动过后的对象。</p>
<p>HotSpot 虚拟机是通过句柄（handle）来完成上述需求的。这里句柄指的是内存中 Java 对象的指针的指针。当发生垃圾回收时，如果 Java 对象被移动了，那么句柄指向的指针值也将发生变动，但句柄本身保持不变。</p>
<p>实际上，无论是局部引用还是全局引用，都是句柄。其中，局部引用所对应的句柄有两种存储方式，一是在本地方法栈帧中，主要用于存放 C 函数所接收的来自 Java 层面的引用类型参数；另一种则是线程私有的句柄块，主要用于存放 C 函数运行过程中创建的局部引用。</p>
<p>当从 C 函数返回至 Java 方法时，本地方法栈帧中的句柄将会被自动清除。而线程私有句柄块则需要由 Java 虚拟机显式清理。</p>
<p>进入 C 函数时对引用类型参数的句柄化，和调整参数位置（C 调用和 Java 调用传参的方式不一样），以及从 C 函数返回时清理线程私有句柄块，共同造就了 JNI 调用的额外性能开销（具体可参考该 stackoverflow 上的<a href="https://stackoverflow.com/questions/24746776/what-does-a-jvm-have-to-do-when-calling-a-native-method/24747484#24747484">回答</a>）。</p>
<h2>总结与实践</h2>
<p>今天我介绍了 JNI 的运行机制。</p>
<p>Java 中的 native 方法的链接方式主要有两种。一是按照 JNI 的默认规范命名所要链接的 C 函数，并依赖于 Java 虚拟机自动链接。另一种则是在 C 代码中主动链接。</p>
<p>JNI 提供了一系列 API 来允许 C 代码使用 Java 语言特性。这些 API 不仅使用了特殊的数据结构来表示 Java 类，还拥有特殊的异常处理模式。</p>
<p>JNI 中的引用可分为局部引用和全局引用。这两者都可以阻止垃圾回收器回收被引用的 Java 对象。不同的是，局部引用在 native 方法调用返回之后便会失效。传入参数以及大部分 JNI API 函数的返回值都属于局部引用。</p>
<hr />
<p>今天的实践环节，请阅读<a href="https://www.ibm.com/developerworks/java/library/j-jni/index.html">该文档</a>中的 Performance pitfalls 以及 Correctness pitfalls 两节。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="31&#32;&#32;Java虚拟机的监控及诊断工具（GUI篇）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="33&#32;&#32;Java&#32;Agent与字节码注入.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435824f961645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
