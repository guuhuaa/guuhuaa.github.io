<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>33  动手实现一个简单的RPC框架（三）：客户端.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;优秀的程序员，你的技术栈中不能只有“增删改查”.md">00 开篇词  优秀的程序员，你的技术栈中不能只有“增删改查”.md</a>

                </li>
                <li>

                    
                    <a href="00&#32;预习&#32;&#32;怎样更好地学习这门课？.md">00 预习  怎样更好地学习这门课？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;为什么需要消息队列？.md">01  为什么需要消息队列？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;该如何选择消息队列？.md">02  该如何选择消息队列？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;消息模型：主题和队列有什么区别？.md">03  消息模型：主题和队列有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;如何利用事务消息实现分布式事务？.md">04  如何利用事务消息实现分布式事务？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何确保消息不会丢失.md">05  如何确保消息不会丢失.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;如何处理消费过程中的重复消息？.md">06  如何处理消费过程中的重复消息？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;消息积压了该如何处理？.md">07  消息积压了该如何处理？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;答疑解惑（一）&#32;&#32;网关如何接收服务端的秒杀结果？.md">08  答疑解惑（一）  网关如何接收服务端的秒杀结果？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;学习开源代码该如何入手？.md">09  学习开源代码该如何入手？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;如何使用异步设计提升系统性能？.md">10  如何使用异步设计提升系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;如何实现高性能的异步网络传输？.md">11  如何实现高性能的异步网络传输？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;序列化与反序列化：如何通过网络传输结构化的数据？.md">12  序列化与反序列化：如何通过网络传输结构化的数据？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;传输协议：应用程序之间对话的语言.md">13  传输协议：应用程序之间对话的语言.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;内存管理：如何避免内存溢出和频繁的垃圾回收？.md">14  内存管理：如何避免内存溢出和频繁的垃圾回收？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;Kafka如何实现高性能IO？.md">15  Kafka如何实现高性能IO？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;缓存策略：如何使用缓存来减少磁盘IO？.md">16  缓存策略：如何使用缓存来减少磁盘IO？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何正确使用锁保护共享数据，协调异步线程？.md">17  如何正确使用锁保护共享数据，协调异步线程？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何用硬件同步原语（CAS）替代锁？.md">18  如何用硬件同步原语（CAS）替代锁？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;数据压缩：时间换空间的游戏.md">19  数据压缩：时间换空间的游戏.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;RocketMQ&#32;Producer源码分析：消息生产的实现过程.md">20  RocketMQ Producer源码分析：消息生产的实现过程.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Kafka&#32;Consumer源码分析：消息消费的实现过程.md">21  Kafka Consumer源码分析：消息消费的实现过程.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;Kafka和RocketMQ的消息复制实现的差异点在哪？.md">22  Kafka和RocketMQ的消息复制实现的差异点在哪？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;RocketMQ客户端如何在集群中找到正确的节点？.md">23  RocketMQ客户端如何在集群中找到正确的节点？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;Kafka的协调服务ZooKeeper：实现分布式系统的“瑞士军刀”.md">24  Kafka的协调服务ZooKeeper：实现分布式系统的“瑞士军刀”.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;RocketMQ与Kafka中如何实现事务？.md">25  RocketMQ与Kafka中如何实现事务？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;MQTT协议：如何支持海量的在线IoT设备.md">26  MQTT协议：如何支持海量的在线IoT设备.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;Pulsar的存储计算分离设计：全新的消息队列设计思路.md">27  Pulsar的存储计算分离设计：全新的消息队列设计思路.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;答疑解惑（二）：我的100元哪儿去了？.md">28  答疑解惑（二）：我的100元哪儿去了？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;流计算与消息（一）：通过Flink理解流计算的原理.md">29  流计算与消息（一）：通过Flink理解流计算的原理.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;流计算与消息（二）：在流计算中使用Kafka链接计算任务.md">30  流计算与消息（二）：在流计算中使用Kafka链接计算任务.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;动手实现一个简单的RPC框架（一）：原理和程序的结构.md">31  动手实现一个简单的RPC框架（一）：原理和程序的结构.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;动手实现一个简单的RPC框架（二）：通信与序列化.md">32  动手实现一个简单的RPC框架（二）：通信与序列化.md</a>

                </li>
                <li>

                    <a class="current-tab" href="33&#32;&#32;动手实现一个简单的RPC框架（三）：客户端.md">33  动手实现一个简单的RPC框架（三）：客户端.md</a>
                    

                </li>
                <li>

                    
                    <a href="34&#32;&#32;动手实现一个简单的RPC框架（四）：服务端.md">34  动手实现一个简单的RPC框架（四）：服务端.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;答疑解惑（三）：主流消息队列都是如何存储消息的？.md">35  答疑解惑（三）：主流消息队列都是如何存储消息的？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;JMQ的Broker是如何异步处理消息的？.md">加餐  JMQ的Broker是如何异步处理消息的？.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;程序员如何构建知识体系？.md">结束语  程序员如何构建知识体系？.md</a>

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
                        <div><h1>33  动手实现一个简单的RPC框架（三）：客户端</h1>
<p>你好，我是李玥。</p>
<p>上节课我们已经一起实现了这个 RPC 框架中的两个基础组件：序列化和网络传输部分，这节课我们继续来实现这个 RPC 框架的客户端部分。</p>
<p>在《[31 | 动手实现一个简单的 RPC 框架（一）：原理和程序的结构]》这节课中我们提到过，在 RPC 框架中，最关键的就是理解“桩”的实现原理，桩是 RPC 框架在客户端的服务代理，它和远程服务具有相同的方法签名，或者说是实现了相同的接口，客户端在调用 RPC 框架提供的服务时，实际调用的就是“桩”提供的方法，在桩的实现方法中，它会发请求到服务端获取调用结果并返回给调用方。</p>
<p><strong>在 RPC 框架的客户端中，最关键的部分，也就是如何来生成和实现这个桩。</strong></p>
<h2>如何来动态地生成桩？</h2>
<p>RPC 框架中的这种桩的设计，它其实采用了一种设计模式：“代理模式”。代理模式给某一个对象提供一个代理对象，并由代理对象控制对原对象的引用，被代理的那个对象称为委托对象。</p>
<p>在 RPC 框架中，代理对象都是由 RPC 框架的客户端来提供的，也就是我们一直说的“桩”，委托对象就是在服务端，真正实现业务逻辑的服务类的实例。</p>
<p><img src="assets/6ca3f88f1a6c06513d5adfe976efcc48.jpg" alt="img" /></p>
<p>我们最常用 Spring 框架，它的核心 IOC（依赖注入）和 AOP（面向切面）机制，就是这种代理模式的一个实现。我们在日常开发的过程中，可以利用这种代理模式，在调用流程中动态地注入一些非侵入式业务逻辑。</p>
<p>这里的“非侵入”指的是，在现有的调用链中，增加一些业务逻辑，而不用去修改调用链上下游的代码。比如说，我们要监控一个方法 A 的请求耗时，普通的方式就是在方法的开始和返回这两个地方各加一条记录时间的语句，这种方法就需要修改这个方法的代码，这是一种“侵入式”的方式。</p>
<p>我们还可以给这个方法所在的类创建一个代理类，在这个代理类的 A 方法中，先记录开始时间，然后调用委托类的 A 方法，再记录结束时间。把这个代理类加入到调用链中，就可以实现“非侵入式”记录耗时了。同样的方式，我们还可以用在权限验证、风险控制、调用链跟踪等等这些场景中。</p>
<p>下面我们来看下，在我们这个 RPC 框架的客户端中，怎么来实现的这个代理类，也就是“桩”。首先我们先定一个 StubFactory 接口，这个接口就只有一个方法：</p>
<pre><code>public interface StubFactory {
    &lt;T&gt; T createStub(Transport transport, Class&lt;T&gt; serviceClass);
}
</code></pre>
<p>这个桩工厂接口只定义了一个方法 createStub，它的功能就是创建一个桩的实例，这个桩实现的接口可以是任意类型的，也就是上面代码中的泛型 T。这个方法有两个参数，第一个参数是一个 Transport 对象，这个 Transport 我们在上节课介绍过，它是用来给服务端发请求的时候使用的。第二个参数是一个 Class 对象，它用来告诉桩工厂：我需要你给我创建的这个桩，应该是什么类型的。createStub 的返回值就是由工厂创建出来的桩。</p>
<p>如何来实现这个工厂方法，创建桩呢？这个桩它是一个由 RPC 框架生成的类，这个类它要实现给定的接口，里面的逻辑就是把方法名和参数封装成请求，发送给服务端，然后再把服务端返回的调用结果返回给调用方。这里我们已经解决了网络传输和序列化的问题，剩下一个核心问题就是如何来生成这个类了。</p>
<p>我们知道，普通的类它是由我们编写的源代码，通过编译器编译之后生成的。那 RPC 框架怎么才能根据要实现的接口来生成一个类呢？在这一块儿，不同的 RPC 框架的实现是不一样的，比如，gRPC 它是在编译 IDL 的时候就把桩生成好了，这个时候编译出来桩，它是目标语言的源代码文件。比如说，目标语言是 Java，编译完成后它们会生成一些 Java 的源代码文件，其中以 Grpc.java 结尾的文件就是生成的桩的源代码。这些生成的源代码文件再经过 Java 编译器编译以后，就成了桩。</p>
<p>而 Dubbo 是在运行时动态生成的桩，这个实现就更加复杂了，并且它利用了很多 Java 语言底层的特性。但是它的原理并不复杂，Java 源代码编译完成之后，生成的是一些 class 文件，JVM 在运行的时候，读取这些 Class 文件来创建对应类的实例。</p>
<p>这个 Class 文件虽然非常复杂，但本质上，它里面记录的内容，就是我们编写的源代码中的内容，包括类的定义，方法定义和业务逻辑等等，并且它也是有固定的格式的。如果说，我们按照这个格式，来生成一个 class 文件，只要这个文件的格式是符合 Java 规范的，JVM 就可以识别并加载它。这样就不需要经过源代码、编译这些过程，直接动态来创建一个桩。</p>
<p>由于动态生成 class 文件这部分逻辑和 Java 语言的特性是紧密关联的，考虑有些同学并不熟悉 Java 语言，所以在这个 RPC 的例子中，我们采用一种更通用的方式来动态生成桩。我们采用的方式是：先生成桩的源代码，然后动态地编译这个生成的源代码，然后再加载到 JVM 中。</p>
<p>为了让这部分代码不会过于复杂，便于你快速理解，我们限定：服务接口只能有一个方法，并且这个方法只能有一个参数，参数和返回值的类型都是 String 类型。你在学会这部分动态生成桩的原理之后，很容易重构这部分代码来解除这个限定，无非是多遍历几次方法和参数而已。</p>
<p>我之前讲过，我们需要动态生成的这个桩，它每个方法的逻辑都是一样的，都是把类名、方法名和方法的参数封装成请求，然后发给服务端，收到服务端响应之后再把结果作为返回值，返回给调用方。所以，我们定义一个 AbstractStub 的抽象类，在这个类中实现大部分通用的逻辑，让所有动态生成的桩都继承这个抽象类，这样动态生成桩的代码会更少一些。</p>
<p>下面我们来实现客户端最关键的这部分代码：实现这个 StubFactory 接口动态生成桩。</p>
<pre><code>public class DynamicStubFactory implements StubFactory{
    private final static String STUB_SOURCE_TEMPLATE =
            &quot;package com.github.liyue2008.rpc.client.stubs;\n&quot; +
            &quot;import com.github.liyue2008.rpc.serialize.SerializeSupport;\n&quot; +
            &quot;\n&quot; +
            &quot;public class %s extends AbstractStub implements %s {\n&quot; +
            &quot;    @Override\n&quot; +
            &quot;    public String %s(String arg) {\n&quot; +
            &quot;        return SerializeSupport.parse(\n&quot; +
            &quot;                invokeRemote(\n&quot; +
            &quot;                        new RpcRequest(\n&quot; +
            &quot;                                \&quot;%s\&quot;,\n&quot; +
            &quot;                                \&quot;%s\&quot;,\n&quot; +
            &quot;                                SerializeSupport.serialize(arg)\n&quot; +
            &quot;                        )\n&quot; +
            &quot;                )\n&quot; +
            &quot;        );\n&quot; +
            &quot;    }\n&quot; +
            &quot;}&quot;;
 
    @Override
    @SuppressWarnings(&quot;unchecked&quot;)
    public &lt;T&gt; T createStub(Transport transport, Class&lt;T&gt; serviceClass) {
        try {
            // 填充模板
            String stubSimpleName = serviceClass.getSimpleName() + &quot;Stub&quot;;
            String classFullName = serviceClass.getName();
            String stubFullName = &quot;com.github.liyue2008.rpc.client.stubs.&quot; + stubSimpleName;
            String methodName = serviceClass.getMethods()[0].getName();
 
            String source = String.format(STUB_SOURCE_TEMPLATE, stubSimpleName, classFullName, methodName, classFullName, methodName);
            // 编译源代码
            JavaStringCompiler compiler = new JavaStringCompiler();
            Map&lt;String, byte[]&gt; results = compiler.compile(stubSimpleName + &quot;.java&quot;, source);
            // 加载编译好的类
            Class&lt;?&gt; clazz = compiler.loadClass(stubFullName, results);
            // 把 Transport 赋值给桩
            ServiceStub stubInstance = (ServiceStub) clazz.newInstance();
            stubInstance.setTransport(transport);
            // 返回这个桩
            return (T) stubInstance;
        } catch (Throwable t) {
            throw new RuntimeException(t);
        }
    }
}
</code></pre>
<p>一起来看一下这段代码，静态变量 STUB_SOURCE_TEMPLATE 是桩的源代码的模板，我们需要做的就是，填充模板中变量，生成桩的源码，然后动态的编译、加载这个桩就可以了。</p>
<p>先来看这个模板，它唯一的这个方法中，就只有一行代码，把接口的类名、方法名和序列化后的参数封装成一个 RpcRequest 对象，调用父类 AbstractStub 中的 invokeRemote 方法，发送给服务端。invokeRemote 方法的返回值就是序列化的调用结果，我们在模板中把这个结果反序列化之后，直接作为返回值返回给调用方就可以了。</p>
<p>再来看下面的 createStrub 方法，从 serviceClass 这个参数中，可以取到服务接口定义的所有信息，包括接口名、它有哪些方法、每个方法的参数和返回值类型等等。通过这些信息，我们就可以来填充模板，生成桩的源代码。</p>
<p>桩的类名就定义为：“接口名 + Stub”，为了避免类名冲突，我们把这些桩都统一放到固定的包 com.github.liyue2008.rpc.client.stubs 下面。填充好模板生成的源代码存放在 source 变量中，然后经过动态编译、动态加载之后，我们就可以拿到这个桩的类 clazz，利用反射创建一个桩的实例 stubInstance。把用于网络传输的对象 transport 赋值给桩，这样桩才能与服务端进行通信。到这里，我们就实现了动态创建一个桩。</p>
<h2>使用依赖倒置原则解耦调用者和实现</h2>
<p>在这个 RPC 框架的例子中，很多地方我们都采用了同样一种解耦的方法：通过定义一个接口来解耦调用方和实现。在设计上这种方法称为“依赖倒置原则（Dependence Inversion Principle）”，它的核心思想是，调用方不应依赖于具体实现，而是为实现定义一个接口，让调用方和实现都依赖于这个接口。这种方法也称为“面向接口编程”。它的好处我们之前已经反复说过了，可以解耦调用方和具体的实现，不仅实现是可替换的，实现连同定义实现的接口也是可以复用的。</p>
<p>比如，我们上面定义的 StubFactory 它是一个接口，它的实现类是 DynamicStubFactory，调用方是 NettyRpcAccessPoint，调用方 NettyAccessPoint 并不依赖实现类 DynamicStubFactory，就可以调用 DynamicStubFactory 的 createStub 方法。</p>
<p>要解耦调用方和实现类，还需要解决一个问题：谁来创建实现类的实例？一般来说，都是谁使用谁创建，但这里面我们为了解耦调用方和实现类，调用方就不能来直接创建实现类，因为这样就无法解耦了。那能不能用一个第三方来创建这个实现类呢？也是不行的，即使用一个第三方类来创建实现，那依赖关系就变成了：调用方依赖第三方类，第三方类依赖实现类，调用方还是间接依赖实现类，还是没有解耦。</p>
<p>这个问题怎么来解决？没错，使用 Spring 的依赖注入是可以解决的。这里再给你介绍一种 Java 语言内置的，更轻量级的解决方案：SPI（Service Provider Interface）。在 SPI 中，每个接口在目录 META-INF/services/ 下都有一个配置文件，文件名就是以这个接口的类名，文件的内容就是它的实现类的类名。还是以 StubFactory 接口为例，我们看一下它的配置文件：</p>
<pre><code>$cat rpc-netty/src/main/resources/META-INF/services/com.github.liyue2008.rpc.client.StubFactory
com.github.liyue2008.rpc.client.DynamicStubFactory
</code></pre>
<p>只要把这个配置文件、接口和实现类都放到 CLASSPATH 中，就可以通过 SPI 的方式来进行加载了。加载的参数就是这个接口的 class 对象，返回值就是这个接口的所有实现类的实例，这样就在“不依赖实现类”的前提下，获得了一个实现类的实例。具体的实现代码在 ServiceSupport 这个类中。</p>
<h2>小结</h2>
<p>这节课我们一起实现了这个 RPC 框架的客户端，在客户端中，最核心的部分就是桩，也就是远程服务的代理类。在桩中，每个方法的逻辑都是一样的，就是把接口名、方法名和请求的参数封装成一个请求发给服务端，由服务端调用真正的业务类获取结果并返回给客户端的桩，桩再把结果返回给调用方。</p>
<p>客户端实现的难点就是，如何来动态地生成桩。像 gRPC 这类多语言的 RPC 框架，都是在编译 IDL 的过程中生成桩的源代码，再和业务代码，使用目标语言的编译器一起编译的。而像 Dubbo 这类没有编译过程的 RPC 框架，都是在运行时，利用一些语言动态特性，动态创建的桩。</p>
<p>RPC 框架的这种“桩”的设计，其实是一种动态代理设计模式。这种设计模式可以在不修改源码，甚至不需要源码的情况下，在调用链中注入一些业务逻辑。这是一种非常有用的高级技巧，可以用在权限验证、风险控制、调用链跟踪等等很多场景中，希望你能掌握它的实现原理。</p>
<p>最后我们介绍的依赖倒置原则，可以非常有效地降低系统各部分之间的耦合度，并且不会过度增加系统的复杂度，建议你在设计软件的时候广泛的采用。其实你想一下，现在这么流行的微服务思想，其实就是依赖倒置原则的实践。只是在微服务中，它更极端地把调用方和实现分离成了不同的软件项目，实现了完全的解耦。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="32&#32;&#32;动手实现一个简单的RPC框架（二）：通信与序列化.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="34&#32;&#32;动手实现一个简单的RPC框架（四）：服务端.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4356c0fa61645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%E9%AB%98%E6%89%8B%E8%AF%BE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
