<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04  JVM是如何执行方法调用的？（上）.md</title>
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

                    <a class="current-tab" href="04&#32;&#32;JVM是如何执行方法调用的？（上）.md">04  JVM是如何执行方法调用的？（上）.md</a>
                    

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
                        <div><h1>04  JVM是如何执行方法调用的？（上）</h1>
<p>前不久在写代码的时候，我不小心踩到一个可变长参数的坑。你或许已经猜到了，它正是可变长参数方法的重载造成的。（注：官方文档建议避免重载可变长参数方法，见 [1] 的最后一段。）</p>
<p>我把踩坑的过程放在了文稿里，你可以点击查看。</p>
<pre><code>void invoke(Object obj, Object... args) { ... }
void invoke(String s, Object obj, Object... args) { ... }
 
invoke(null, 1);    // 调用第二个 invoke 方法
invoke(null, 1, 2); // 调用第二个 invoke 方法
invoke(null, new Object[]{1}); // 只有手动绕开可变长参数的语法糖，
                               // 才能调用第一个 invoke 方法
 
</code></pre>
<p>当时情况是这样子的，某个 API 定义了两个同名的重载方法。其中，第一个接收一个 Object，以及声明为 Object…的变长参数；而第二个则接收一个 String、一个 Object，以及声明为 Object…的变长参数。</p>
<p>这里我想调用第一个方法，传入的参数为 (null, 1)。也就是说，声明为 Object 的形式参数所对应的实际参数为 null，而变长参数则对应 1。</p>
<p>通常来说，之所以不提倡可变长参数方法的重载，是因为 Java 编译器可能无法决定应该调用哪个目标方法。</p>
<p>在这种情况下，编译器会报错，并且提示这个方法调用有二义性。然而，Java 编译器直接将我的方法调用识别为调用第二个方法，这究竟是为什么呢？</p>
<p>带着这个问题，我们来看一看 Java 虚拟机是怎么识别目标方法的。</p>
<h2>重载与重写</h2>
<p>在 Java 程序里，如果同一个类中出现多个名字相同，并且参数类型相同的方法，那么它无法通过编译。也就是说，在正常情况下，如果我们想要在同一个类中定义名字相同的方法，那么它们的参数类型必须不同。这些方法之间的关系，我们称之为重载。</p>
<pre><code>小知识：这个限制可以通过字节码工具绕开。也就是说，在编译完成之后，我们可以再向 class 文件中添加方法名和参数类型相同，而返回类型不同的方法。当这种包括多个方法名相同、参数类型相同，而返回类型不同的方法的类，出现在 Java 编译器的用户类路径上时，它是怎么确定需要调用哪个方法的呢？当前版本的 Java 编译器会直接选取第一个方法名以及参数类型匹配的方法。并且，它会根据所选取方法的返回类型来决定可不可以通过编译，以及需不需要进行值转换等。
</code></pre>
<p>重载的方法在编译过程中即可完成识别。具体到每一个方法调用，Java 编译器会根据所传入参数的声明类型（注意与实际类型区分）来选取重载方法。选取的过程共分为三个阶段：</p>
<ol>
<li>在不考虑对基本类型自动装拆箱（auto-boxing，auto-unboxing），以及可变长参数的情况下选取重载方法；</li>
<li>如果在第 1 个阶段中没有找到适配的方法，那么在允许自动装拆箱，但不允许可变长参数的情况下选取重载方法；</li>
<li>如果在第 2 个阶段中没有找到适配的方法，那么在允许自动装拆箱以及可变长参数的情况下选取重载方法。</li>
</ol>
<p>如果 Java 编译器在同一个阶段中找到了多个适配的方法，那么它会在其中选择一个最为贴切的，而决定贴切程度的一个关键就是形式参数类型的继承关系。</p>
<p>在开头的例子中，当传入 null 时，它既可以匹配第一个方法中声明为 Object 的形式参数，也可以匹配第二个方法中声明为 String 的形式参数。由于 String 是 Object 的子类，因此 Java 编译器会认为第二个方法更为贴切。</p>
<p>除了同一个类中的方法，重载也可以作用于这个类所继承而来的方法。也就是说，如果子类定义了与父类中非私有方法同名的方法，而且这两个方法的参数类型不同，那么在子类中，这两个方法同样构成了重载。</p>
<p>那么，如果子类定义了与父类中非私有方法同名的方法，而且这两个方法的参数类型相同，那么这两个方法之间又是什么关系呢？</p>
<p>如果这两个方法都是静态的，那么子类中的方法隐藏了父类中的方法。如果这两个方法都不是静态的，且都不是私有的，那么子类的方法重写了父类中的方法。</p>
<p>众所周知，Java 是一门面向对象的编程语言，它的一个重要特性便是多态。而方法重写，正是多态最重要的一种体现方式：它允许子类在继承父类部分功能的同时，拥有自己独特的行为。</p>
<p>打个比方，如果你经常漫游，那么你可能知道，拨打 10086 会根据你当前所在地，连接到当地的客服。重写调用也是如此：它会根据调用者的动态类型，来选取实际的目标方法。</p>
<h2>JVM 的静态绑定和动态绑定</h2>
<p>接下来，我们来看看 Java 虚拟机是怎么识别方法的。</p>
<p>Java 虚拟机识别方法的关键在于类名、方法名以及方法描述符（method descriptor）。前面两个就不做过多的解释了。至于方法描述符，它是由方法的参数类型以及返回类型所构成。在同一个类中，如果同时出现多个名字相同且描述符也相同的方法，那么 Java 虚拟机会在类的验证阶段报错。</p>
<p>可以看到，Java 虚拟机与 Java 语言不同，它并不限制名字与参数类型相同，但返回类型不同的方法出现在同一个类中，对于调用这些方法的字节码来说，由于字节码所附带的方法描述符包含了返回类型，因此 Java 虚拟机能够准确地识别目标方法。</p>
<p>Java 虚拟机中关于方法重写的判定同样基于方法描述符。也就是说，如果子类定义了与父类中非私有、非静态方法同名的方法，那么只有当这两个方法的参数类型以及返回类型一致，Java 虚拟机才会判定为重写。</p>
<p>对于 Java 语言中重写而 Java 虚拟机中非重写的情况，编译器会通过生成桥接方法 [2] 来实现 Java 中的重写语义。</p>
<p>由于对重载方法的区分在编译阶段已经完成，我们可以认为 Java 虚拟机不存在重载这一概念。因此，在某些文章中，重载也被称为静态绑定（static binding），或者编译时多态（compile-time polymorphism）；而重写则被称为动态绑定（dynamic binding）。</p>
<p>这个说法在 Java 虚拟机语境下并非完全正确。这是因为某个类中的重载方法可能被它的子类所重写，因此 Java 编译器会将所有对非私有实例方法的调用编译为需要动态绑定的类型。</p>
<p>确切地说，Java 虚拟机中的静态绑定指的是在解析时便能够直接识别目标方法的情况，而动态绑定则指的是需要在运行过程中根据调用者的动态类型来识别目标方法的情况。</p>
<p>具体来说，Java 字节码中与调用相关的指令共有五种。</p>
<ol>
<li>invokestatic：用于调用静态方法。</li>
<li>invokespecial：用于调用私有实例方法、构造器，以及使用 super 关键字调用父类的实例方法或构造器，和所实现接口的默认方法。</li>
<li>invokevirtual：用于调用非私有实例方法。</li>
<li>invokeinterface：用于调用接口方法。</li>
<li>invokedynamic：用于调用动态方法。</li>
</ol>
<p>由于 invokedynamic 指令较为复杂，我将在后面的篇章中单独介绍。这里我们只讨论前四种。</p>
<p>我在文章中贴了一段代码，展示了编译生成这四种调用指令的情况。</p>
<pre><code>interface 客户 {
  boolean isVIP();
}
 
class 商户 {
  public double 折后价格 (double 原价, 客户 某客户) {
    return 原价 * 0.8d;
  }
}
 
class 奸商 extends 商户 {
  @Override
  public double 折后价格 (double 原价, 客户 某客户) {
    if (某客户.isVIP()) {                         // invokeinterface      
      return 原价 * 价格歧视 ();                    // invokestatic
    } else {
      return super. 折后价格 (原价, 某客户);          // invokespecial
    }
  }
  public static double 价格歧视 () {
    // 咱们的杀熟算法太粗暴了，应该将客户城市作为随机数生成器的种子。
    return new Random()                          // invokespecial
           .nextDouble()                         // invokevirtual
           + 0.8d;
  }
}
</code></pre>
<p>在代码中，“商户”类定义了一个成员方法，叫做“折后价格”，它将接收一个 double 类型的参数，以及一个“客户”类型的参数。这里“客户”是一个接口，它定义了一个接口方法，叫“isVIP”。</p>
<p>我们还定义了另一个叫做“奸商”的类，它继承了“商户”类，并且重写了“折后价格”这个方法。如果客户是 VIP，那么它会被给到一个更低的折扣。</p>
<p>在这个方法中，我们首先会调用“客户”接口的”isVIP“方法。该调用会被编译为 invokeinterface 指令。</p>
<p>如果客户是 VIP，那么我们会调用奸商类的一个名叫“价格歧视”的静态方法。该调用会被编译为 invokestatic 指令。如果客户不是 VIP，那么我们会通过 super 关键字调用父类的“折后价格”方法。该调用会被编译为 invokespecial 指令。</p>
<p>在静态方法“价格歧视”中，我们会调用 Random 类的构造器。该调用会被编译为 invokespecial 指令。然后我们会以这个新建的 Random 对象为调用者，调用 Random 类中的 nextDouble 方法。该调用会被编译为 invokevirutal 指令。</p>
<p>对于 invokestatic 以及 invokespecial 而言，Java 虚拟机能够直接识别具体的目标方法。</p>
<p>而对于 invokevirtual 以及 invokeinterface 而言，在绝大部分情况下，虚拟机需要在执行过程中，根据调用者的动态类型，来确定具体的目标方法。</p>
<p>唯一的例外在于，如果虚拟机能够确定目标方法有且仅有一个，比如说目标方法被标记为 final[3][4]，那么它可以不通过动态类型，直接确定目标方法。</p>
<h2>调用指令的符号引用</h2>
<p>在编译过程中，我们并不知道目标方法的具体内存地址。因此，Java 编译器会暂时用符号引用来表示该目标方法。这一符号引用包括目标方法所在的类或接口的名字，以及目标方法的方法名和方法描述符。</p>
<p>符号引用存储在 class 文件的常量池之中。根据目标方法是否为接口方法，这些引用可分为接口符号引用和非接口符号引用。我在文章中贴了一个例子，利用“javap -v”打印某个类的常量池，如果你感兴趣的话可以到文章中查看。</p>
<pre><code>// 在奸商.class 的常量池中，#16 为接口符号引用，指向接口方法 &quot; 客户.isVIP()&quot;。而 #22 为非接口符号引用，指向静态方法 &quot; 奸商. 价格歧视 ()&quot;。
$ javap -v 奸商.class ...
Constant pool:
...
  #16 = InterfaceMethodref #27.#29        // 客户.isVIP:()Z
...
  #22 = Methodref          #1.#33         // 奸商. 价格歧视:()D
...
</code></pre>
<p>上一篇中我曾提到过，在执行使用了符号引用的字节码前，Java 虚拟机需要解析这些符号引用，并替换为实际引用。</p>
<p>对于非接口符号引用，假定该符号引用所指向的类为 C，则 Java 虚拟机会按照如下步骤进行查找。</p>
<ol>
<li>在 C 中查找符合名字及描述符的方法。</li>
<li>如果没有找到，在 C 的父类中继续搜索，直至 Object 类。</li>
<li>如果没有找到，在 C 所直接实现或间接实现的接口中搜索，这一步搜索得到的目标方法必须是非私有、非静态的。并且，如果目标方法在间接实现的接口中，则需满足 C 与该接口之间没有其他符合条件的目标方法。如果有多个符合条件的目标方法，则任意返回其中一个。</li>
</ol>
<p>从这个解析算法可以看出，静态方法也可以通过子类来调用。此外，子类的静态方法会隐藏（注意与重写区分）父类中的同名、同描述符的静态方法。</p>
<p>对于接口符号引用，假定该符号引用所指向的接口为 I，则 Java 虚拟机会按照如下步骤进行查找。</p>
<ol>
<li>在 I 中查找符合名字及描述符的方法。</li>
<li>如果没有找到，在 Object 类中的公有实例方法中搜索。</li>
<li>如果没有找到，则在 I 的超接口中搜索。这一步的搜索结果的要求与非接口符号引用步骤 3 的要求一致。</li>
</ol>
<p>经过上述的解析步骤之后，符号引用会被解析成实际引用。对于可以静态绑定的方法调用而言，实际引用是一个指向方法的指针。对于需要动态绑定的方法调用而言，实际引用则是一个方法表的索引。具体什么是方法表，我会在下一篇中做出解答。</p>
<h2>总结与实践</h2>
<p>今天我介绍了 Java 以及 Java 虚拟机是如何识别目标方法的。</p>
<p>在 Java 中，方法存在重载以及重写的概念，重载指的是方法名相同而参数类型不相同的方法之间的关系，重写指的是方法名相同并且参数类型也相同的方法之间的关系。</p>
<p>Java 虚拟机识别方法的方式略有不同，除了方法名和参数类型之外，它还会考虑返回类型。</p>
<p>在 Java 虚拟机中，静态绑定指的是在解析时便能够直接识别目标方法的情况，而动态绑定则指的是需要在运行过程中根据调用者的动态类型来识别目标方法的情况。由于 Java 编译器已经区分了重载的方法，因此可以认为 Java 虚拟机中不存在重载。</p>
<p>在 class 文件中，Java 编译器会用符号引用指代目标方法。在执行调用指令前，它所附带的符号引用需要被解析成实际引用。对于可以静态绑定的方法调用而言，实际引用为目标方法的指针。对于需要动态绑定的方法调用而言，实际引用为辅助动态绑定的信息。</p>
<p>在文中我曾提到，Java 的重写与 Java 虚拟机中的重写并不一致，但是编译器会通过生成桥接方法来弥补。今天的实践环节，我们来看一下两个生成桥接方法的例子。你可以通过“javap -v”来查看 class 文件所包含的方法。</p>
<ol>
<li>重写方法的返回类型不一致：</li>
</ol>
<pre><code>interface Customer {
  boolean isVIP();
}
 
class Merchant {
  public Number actionPrice(double price, Customer customer) {
    ...
  }
}
 
class NaiveMerchant extends Merchant {
  @Override
  public Double actionPrice(double price, Customer customer) {
    ...
  }
}
</code></pre>
<ol>
<li>范型参数类型造成的方法参数类型不一致：</li>
</ol>
<pre><code>interface Customer {
  boolean isVIP();
}
 
class Merchant&lt;T extends Customer&gt; {
 	public double actionPrice(double price, T customer) {
		  ...
 	}
}
 
class VIPOnlyMerchant extends Merchant&lt;VIP&gt; {
	 @Override
 	public double actionPrice(double price, VIP customer) {
    ...
 	}
}
</code></pre>
<p><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/language/varargs.html">https://docs.oracle.com/javase/8/docs/technotes/guides/language/varargs.html</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/bridgeMethods.html">https://docs.oracle.com/javase/tutorial/java/generics/bridgeMethods.html</a>
<a href="https://wiki.openjdk.java.net/display/HotSpot/VirtualCalls">https://wiki.openjdk.java.net/display/HotSpot/VirtualCalls</a>
<a href="https://wiki.openjdk.java.net/display/HotSpot/InterfaceCalls">https://wiki.openjdk.java.net/display/HotSpot/InterfaceCalls</a></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;&#32;Java虚拟机是如何加载Java类的.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;&#32;JVM是如何执行方法调用的？（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435774bb1c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
