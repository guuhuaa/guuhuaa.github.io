<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（上）.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;领略&#32;MyBatis&#32;设计思维，突破持久化技术瓶颈.md">00 开篇词  领略 MyBatis 设计思维，突破持久化技术瓶颈.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;常见持久层框架赏析，到底是什么让你选择&#32;MyBatis？.md">01  常见持久层框架赏析，到底是什么让你选择 MyBatis？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;订单系统持久层示例分析，20&#32;分钟带你快速上手&#32;MyBatis.md">02  订单系统持久层示例分析，20 分钟带你快速上手 MyBatis.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;MyBatis&#32;源码环境搭建及整体架构解析.md">03  MyBatis 源码环境搭建及整体架构解析.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;MyBatis&#32;反射工具箱：带你领略不一样的反射设计思路.md">04  MyBatis 反射工具箱：带你领略不一样的反射设计思路.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;数据库类型体系与&#32;Java&#32;类型体系之间的“爱恨情仇”.md">05  数据库类型体系与 Java 类型体系之间的“爱恨情仇”.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;日志框架千千万，MyBatis&#32;都能兼容的秘密是什么？.md">06  日志框架千千万，MyBatis 都能兼容的秘密是什么？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入数据源和事务，把握持久化框架的两个关键命脉.md">07  深入数据源和事务，把握持久化框架的两个关键命脉.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;Mapper&#32;文件与&#32;Java&#32;接口的优雅映射之道.md">08  Mapper 文件与 Java 接口的优雅映射之道.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;基于&#32;MyBatis&#32;缓存分析装饰器模式的最佳实践.md">09  基于 MyBatis 缓存分析装饰器模式的最佳实践.md</a>

                </li>
                <li>

                    <a class="current-tab" href="10&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（上）.md">10  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（上）.md</a>
                    

                </li>
                <li>

                    
                    <a href="11&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（下）.md">11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（上）.md">12  深入分析动态 SQL 语句解析全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（下）.md">13  深入分析动态 SQL 语句解析全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（上）.md">14  探究 MyBatis 结果集映射机制背后的秘密（上）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（下）.md">15  探究 MyBatis 结果集映射机制背后的秘密（下）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;StatementHandler：参数绑定、SQL&#32;执行和结果映射的奠基者.md">16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（上）.md">17  Executor 才是执行 SQL 语句的幕后推手（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（下）.md">18  Executor 才是执行 SQL 语句的幕后推手（下）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;深入&#32;MyBatis&#32;内核与业务逻辑的桥梁——接口层.md">19  深入 MyBatis 内核与业务逻辑的桥梁——接口层.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;插件体系让&#32;MyBatis&#32;世界更加精彩.md">20  插件体系让 MyBatis 世界更加精彩.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深挖&#32;MyBatis&#32;与&#32;Spring&#32;集成底层原理.md">21  深挖 MyBatis 与 Spring 集成底层原理.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;基于&#32;MyBatis&#32;的衍生框架一览.md">22  基于 MyBatis 的衍生框架一览.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;会使用只能默默“搬砖”，懂原理才能快速晋升.md">23 结束语  会使用只能默默“搬砖”，懂原理才能快速晋升.md</a>

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
                        <div><h1>10  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（上）</h1>
<p>很多开源框架之所以能够流行起来，是因为它们解决了领域内的一些通用问题。但在实际使用这些开源框架的时候，我们都是要解决通用问题中的一个特例问题，所以这时我们就需要使用一种方式来控制开源框架的行为，这就是开源框架提供各种各样配置的核心原因之一。</p>
<p>现在控制开源框架行为主流的配置方式就是 XML 配置方式和注解方式。在《02 | 订单系统持久层示例分析，20 分钟带你快速上手 MyBatis》这一讲中我们介绍过，MyBatis 有两方面的 XML 配置，<strong>一个是 mybatis-config.xml 配置文件中的整体配置，另一个是 Mapper.xml 配置文件中的 SQL 语句</strong>。当然，MyBatis 中也有注解，前面的课程中也多少有涉及，其核心实现与 XML 配置基本类似，所以这一讲我们就重点分析 XML 配置的初始化过程，注解相关的内容就留给你自己分析了。</p>
<p>在初始化的过程中，MyBatis 会读取 mybatis-config.xml 这个全局配置文件以及所有的 Mapper 映射配置文件，同时还会加载这两个配置文件中指定的类，解析类中的相关注解，最终将解析得到的信息转换成配置对象。<strong>完成配置加载之后，MyBatis 就会根据得到的配置对象初始化各个模块</strong>。</p>
<p>MyBatis 在加载配置文件、创建配置对象的时候，会使用到经典设计模式中的<strong>构造者模式</strong>，所以下面我们就来先介绍一下构造者模式的知识点。</p>
<h3>构造者模式</h3>
<p>构造者模式最核心的思想就是将创建复杂对象的过程与复杂对象本身进行拆分。通俗来讲，构造者模式是<strong>将复杂对象的创建过程分解成了多个简单步骤，在创建复杂对象的时候，只需要了解复杂对象的基本属性即可，而不需要关心复杂对象的内部构造过程</strong>。这样的话，使用方只需要关心这个复杂对象要什么数据，而不再关心内部细节。</p>
<p>构造者模式的类图如下所示：</p>
<p><img src="assets/Cgp9HWA01CyAP_FuAAGR6B2VRBg565.png" alt="2021223-18655.png" /></p>
<p>构造者模式类图</p>
<p>从图中，我们可以看到构造者模式的四个核心组件。</p>
<ul>
<li>Product 接口：复杂对象的接口，定义了要创建的目标对象的行为。</li>
<li>ProductImpl 类：Product 接口的实现，它真正要创建的复杂对象，其中实现了我们需要的复杂业务逻辑。</li>
<li>Builder 接口：定义了构造 Product 对象的每一步行为。</li>
<li>BuilderImpl 类：Builder 接口的具体实现，其中具体实现了构造一个 Product 的每一个步骤，例如上图中的 setPart1()、setPart2() 等方法，都是用来构造 ProductImpl 对象的各个部分。在完成整个 Product 对象的构造之后，我们会通过 build() 方法返回这个构造好的 Product 对象。</li>
</ul>
<p>使用构造者模式一般有两个目的。第一个目的是<strong>将使用方与复杂对象的内部细节隔离，从而实现解耦的效果</strong>。使用方提供的所有信息，都是由 Builder 这个“中间商”接收的，然后由 Builder 消化这些信息并构造出一个完整可用的 Product 对象。第二个目的是<strong>简化复杂对象的构造过程</strong>。在很多场景中，复杂对象可能有很多默认属性，这时我们就可以将这些默认属性封装到 Builder 中，这样就可以简化创建复杂对象所需的信息。</p>
<p>通过构建者模式的类图我们还可以看出，<strong>每个 BuilderImpl 实现都是能够独立创建出对应的 ProductImpl 对象</strong>，那么在程序需要扩展的时候，我们只需要添加新的 BuilderImpl 和 ProductImpl，就能实现功能的扩展，这完全符合“开放-封闭原则”。</p>
<h3>mybatis-config.xml 解析全流程</h3>
<p>介绍完构造者模式相关的知识点之后，下面我们正式开始介绍 MyBatis 的初始化过程。</p>
<p><strong>MyBatis 初始化的第一个步骤就是加载和解析 mybatis-config.xml 这个全局配置文件</strong>，入口是 XMLConfigBuilder 这个 Builder 对象，它由 SqlSessionFactoryBuilder.build() 方法创建。XMLConfigBuilder 会解析 mybatis-config.xml 配置文件得到对应的 Configuration 全局配置对象，然后 SqlSessionFactoryBuilder 会根据得到的 Configuration 全局配置对象创建一个 DefaultSqlSessionFactory 对象返回给上层使用。</p>
<p>这里<strong>创建的 XMLConfigBuilder 对象的核心功能就是解析 mybatis-config.xml 配置文件</strong>。XMLConfigBuilder 有一部分能力继承自 BaseBuilder 抽象类，具体继承关系如下图所示：</p>
<p><img src="assets/Cgp9HWA01DeAFFn1AAEKQNyimxk937.png" alt="2021223-1877.png" /></p>
<p>BaseBuilder 继承关系图</p>
<p>BaseBuilder 抽象类扮演了构造者模式中 Builder 接口的角色，下面我们先来看 BaseBuilder 中各个字段的定义。</p>
<ul>
<li>configuration（Configuration 类型）：MyBatis 的初始化过程就是围绕 Configuration 对象展开的，我们可以认为 Configuration 是一个单例对象，MyBatis 初始化解析到的全部配置信息都会记录到 Configuration 对象中。</li>
<li>typeAliasRegistry（TypeAliasRegistry 类型）：别名注册中心。比如，《02 讲的订单系统》示例中，我们在 mybatis-config.xml 配置文件中，使用 标签为很多类定义了别名。</li>
<li>typeHandlerRegistry（TypeHandlerRegistry 类型）：TypeHandler 注册中心。除了定义别名之外，我们在 mybatis-config.xml 配置文件中，还可以使用 <code>&lt;typeHandlers&gt;</code> 标签添加自定义 TypeHandler 实现，实现数据库类型与 Java 类型的自定义转换，这些自定义的 TypeHandler 都会记录在这个 TypeHandlerRegistry 对象中。</li>
</ul>
<p>除了关联 Configuration 对象之外，BaseBuilder 还提供了另外两个基本能力：</p>
<ul>
<li><strong>解析别名</strong>，核心逻辑是在 resolveAlias() 方法中实现的，主要依赖于 TypeAliasRegistry 对象；</li>
<li><strong>解析 TypeHandler</strong>，核心逻辑是在 resolveTypeHandler() 方法中实现的，主要依赖于 TypeHandlerRegistry 对象。</li>
</ul>
<p>了解了 BaseBuilder 提供的基础能力之后，我们回到 XMLConfigBuilder 这个 Builder 实现类，看看它是如何解析 mybatis-config.xml 配置文件的。</p>
<p>首先我们来了解一下 XMLConfigBuilder 的核心字段。</p>
<ul>
<li>parsed（boolean 类型）：状态标识字段，记录当前 XMLConfigBuilder 对象是否已经成功解析完 mybatis-config.xml 配置文件。</li>
<li>parser（XPathParser 类型）：XPathParser 对象是一个 XML 解析器，这里的 parser 对象就是用来解析 mybatis-config.xml 配置文件的。</li>
<li>environment（String 类型）： 标签定义的环境名称。</li>
<li>localReflectorFactory（ReflectorFactory 类型）：ReflectorFactory 接口的核心功能是实现对 Reflector 对象的创建和缓存。</li>
</ul>
<p>在 SqlSessionFactoryBuilder.build() 方法中也可以看到，XMLConfigBuilder.parse() 方法触发了 mybatis-config.xml 配置文件的解析，<strong>其中的 parseConfiguration() 方法定义了解析 mybatis-config.xml 配置文件的完整流程</strong>，核心步骤如下：</p>
<ul>
<li>解析 <code>&lt;properties&gt;</code> 标签；</li>
<li>解析 <code>&lt;settings&gt;</code> 标签；</li>
<li>处理日志相关组件；</li>
<li>解析 <code>&lt;typeAliases&gt;</code> 标签；</li>
<li>解析 <code>&lt;plugins&gt;</code> 标签；</li>
<li>解析 <code>&lt;objectFactory&gt;</code> 标签；</li>
<li>解析 <code>&lt;objectWrapperFactory&gt;</code> 标签；</li>
<li>解析 <code>&lt;reflectorFactory&gt;</code> 标签；</li>
<li>解析 <code>&lt;environments&gt;</code> 标签；</li>
<li>解析 <code>&lt;databaseIdProvider&gt;</code> 标签；</li>
<li>解析 <code>&lt;typeHandlers&gt;</code> 标签；</li>
<li>解析 <code>&lt;mappers&gt;</code> 标签。</li>
</ul>
<p>从 parseConfiguration()方法中，我们可以清晰地看到 XMLConfigBuilder 对 mybatis-config.xml 配置文件中各类标签的解析方法，下面我们就逐一介绍这些方法的核心实现。</p>
<h4>1. 处理<code>&lt;properties&gt;</code>标签</h4>
<p>我们可以通过 <code>&lt;properties&gt;</code> 标签定义 KV 信息供 MyBatis 使用，propertiesElement() 方法的核心逻辑就是解析 mybatis-config.xml 配置文件中的 <code>&lt;properties&gt;</code> 标签。</p>
<p>从 <code>&lt;properties&gt;</code> 标签中解析出来的 KV 信息会被记录到一个 Properties 对象（也就是 Configuration 全局配置对象的 variables 字段），在后续解析其他标签的时候，MyBatis 会使用这个 Properties 对象中记录的 KV 信息替换匹配的占位符。</p>
<h4>2. 处理<code>&lt;settings&gt;</code>标签</h4>
<p>MyBatis 中有很多全局性的配置，例如，是否使用二级缓存、是否开启懒加载功能等，这些都是通过 mybatis-config.xml 配置文件中的 <code>&lt;settings&gt;</code> 标签进行配置的。</p>
<p>XMLConfigBuilder.settingsAsProperties() 方法的核心逻辑就是解析 <code>&lt;settings&gt;</code> 标签，并将解析得到的配置信息记录到 Configuration 这个全局配置对象的同名属性中，具体实现如下：</p>
<pre><code>private Properties settingsAsProperties(XNode context) {

    if (context == null) {

        return new Properties();

    }

    // 处理&lt;settings&gt;标签的所有子标签，也就是&lt;setting&gt;标签，将其name属性和value属性

    // 整理到Properties对象中保存

    Properties props = context.getChildrenAsProperties();

    // 创建Configuration对应的MetaClass对象

    MetaClass metaConfig = MetaClass.forClass(Configuration.class, localReflectorFactory);

    // 检测Configuration对象中是否包含每个配置项的setter方法

    for (Object key : props.keySet()) {

        if (!metaConfig.hasSetter(String.valueOf(key))) {

            throw new BuilderException(&quot;The setting &quot; + key + &quot; is not known.  Make sure you spelled it correctly (case sensitive).&quot;);

        }

    }

    return props;

}
</code></pre>
<h4>3. 处理<code>&lt;typeAliases&gt;</code>和<code>&lt;typeHandlers&gt;</code>标签</h4>
<p>XMLConfigBuilder 中提供了 typeAliasesElement() 方法和 typeHandlerElement() 方法，分别用来负责处理 <code>&lt;typeAliases&gt;</code> 标签和 <code>&lt;typeHandlers&gt;</code> 标签，解析得到的别名信息和 TypeHandler 信息就会分别记录到 TypeAliasRegistry 和 TypeHandlerRegistry（前面介绍 BaseHandler 的时候，我们已经简单介绍过这两者了）。</p>
<p>下面我们以 typeHandlerElement() 方法为例来分析一下这个过程：</p>
<pre><code>private void typeHandlerElement(XNode parent) {

    if (parent != null) {

        for (XNode child : parent.getChildren()) { // 处理全部&lt;typeHandler&gt;子标签

            if (&quot;package&quot;.equals(child.getName())) { 

                // 如果指定了package属性，则扫描指定包中所有的类，

                // 并解析@MappedTypes注解，完成TypeHandler的注册

                String typeHandlerPackage = child.getStringAttribute(&quot;name&quot;);

                typeHandlerRegistry.register(typeHandlerPackage);

            } else {

                // 如果没有指定package属性，则尝试获取javaType、jdbcType、handler三个属性

                String javaTypeName = child.getStringAttribute(&quot;javaType&quot;);

                String jdbcTypeName = child.getStringAttribute(&quot;jdbcType&quot;);

                String handlerTypeName = child.getStringAttribute(&quot;handler&quot;);

                // 根据属性确定TypeHandler类型以及它能够处理的数据库类型和Java类型

                Class&lt;?&gt; javaTypeClass = resolveClass(javaTypeName);

                JdbcType jdbcType = resolveJdbcType(jdbcTypeName);

                Class&lt;?&gt; typeHandlerClass = resolveClass(handlerTypeName);

                // 调用TypeHandlerRegistry.register()方法注册TypeHandler

                if (javaTypeClass != null) {

                    if (jdbcType == null) {

                        typeHandlerRegistry.register(javaTypeClass, typeHandlerClass);

                    } else {

                        typeHandlerRegistry.register(javaTypeClass, jdbcType, typeHandlerClass);

                    }

                } else {

                    typeHandlerRegistry.register(typeHandlerClass);

                }

            }

        }

    }

}
</code></pre>
<h4>4. 处理<code>&lt;plugins&gt;</code>标签</h4>
<p>我们知道 MyBatis 是一个非常易于扩展的持久层框架，而<strong>插件就是 MyBatis 提供的一种重要扩展机制</strong>。</p>
<p>我们可以自定义一个实现了 Interceptor 接口的插件来扩展 MyBatis 的行为，或是拦截 MyBatis 的一些默认行为。插件的工作机制我们会在后面的课时中详细分析，这里我们重点来看 MyBatis 初始化过程中插件配置的加载，也就是 XMLConfigBuilder 中的 pluginElement()方法，该方法的核心就是解析 <code>&lt;plugins&gt;</code> 标签中配置的自定义插件，具体实现如下：</p>
<pre><code>private void pluginElement(XNode parent) throws Exception {

    if (parent != null) {

        // 遍历全部的&lt;plugin&gt;子标签

        for (XNode child : parent.getChildren()) {

            // 获取每个&lt;plugin&gt;标签中的interceptor属性

            String interceptor = child.getStringAttribute(&quot;interceptor&quot;);

            // 获取&lt;plugin&gt;标签下的其他配置信息

            Properties properties = child.getChildrenAsProperties();

            // 初始化interceptor属性指定的自定义插件

            Interceptor interceptorInstance = (Interceptor) resolveClass(interceptor).getDeclaredConstructor().newInstance();

            // 初始化插件的配置

            interceptorInstance.setProperties(properties);

            // 将Interceptor对象添加到Configuration的插件链中保存，等待后续使用

            configuration.addInterceptor(interceptorInstance);

        }

    }

}
</code></pre>
<h4>5. 处理<code>&lt;objectFactory&gt;</code>标签</h4>
<p>在前面《04 | MyBatis 反射工具箱：带你领略不一样的反射设计思路》中我们提到过，MyBatis 支持自定义 ObjectFactory 实现类和 ObjectWrapperFactory。XMLConfigBuilder 中的 objectFactoryElement() 方法就实现了加载自定义 ObjectFactory 实现类的功能，其核心逻辑就是解析 <code>&lt;objectFactory&gt;</code> 标签中配置的自定义 ObjectFactory 实现类，并完成相关的实例化操作，相关的代码实现如下：</p>
<pre><code>private void objectFactoryElement(XNode context) throws Exception {

if (context != null) {

    // 获取&lt;objectFactory&gt;标签的type属性

    String type = context.getStringAttribute(&quot;type&quot;);

    // 根据type属性值，初始化自定义的ObjectFactory实现

    ObjectFactory factory = (ObjectFactory) resolveClass(type).getDeclaredConstructor().newInstance();

    // 初始化ObjectFactory对象的配置

    Properties properties = context.getChildrenAsProperties();

    factory.setProperties(properties);

    // 将ObjectFactory对象记录到Configuration这个全局配置对象中

    configuration.setObjectFactory(factory);

}
</code></pre>
<p>除了 <code>&lt;objectFactory&gt;</code> 标签之外，我们还可以通过 <code>&lt;objectWrapperFactory&gt;</code> 标签和 <code>&lt;reflectorFactory&gt;</code> 标签配置自定义的 ObjectWrapperFactory 实现类和 ReflectorFactory 实现类，这两个标签的解析分别对应 objectWrapperFactoryElement() 方法和 reflectorFactoryElement() 方法，两者实现与 objectFactoryElement() 方法实现类似，这里就不再展示，你若感兴趣的话可以参考<a href="https://github.com/xxxlxy2008/mybatis">源码</a>进行学习。</p>
<h4>6. 处理<code>&lt;environments&gt;</code>标签</h4>
<p>在 MyBatis 中，我们可以通过 <code>&lt;environment&gt;</code> 标签为不同的环境添加不同的配置，例如，线上环境、预上线环境、测试环境等，<strong>每个 <environment> 标签只会对应一种特定的环境配置</strong>。</p>
<p>environmentsElement() 方法中实现了 XMLConfigBuilder 处理 <code>&lt;environments&gt;</code> 标签的核心逻辑，它会根据 XMLConfigBuilder.environment 字段值，拿到正确的 <code>&lt;environment&gt;</code> 标签，然后解析这个环境中使用的 TransactionFactory、DataSource 等核心对象，也就知道了 MyBatis 要请求哪个数据库、如何管理事务等信息。</p>
<p>下面是 environmentsElement() 方法的核心逻辑：</p>
<pre><code>private void environmentsElement(XNode context) throws Exception {

    if (context != null) {

        if (environment == null) { // 未指定使用的环境id，默认获取default值 

            environment = context.getStringAttribute(&quot;default&quot;);

        }

        // 获取&lt;environment&gt;标签下的所有配置

        for (XNode child : context.getChildren()) {

            // 获取环境id

            String id = child.getStringAttribute(&quot;id&quot;);

            if (isSpecifiedEnvironment(id)) { 

                // 获取&lt;transactionManager&gt;、&lt;dataSource&gt;等标签，并进行解析，其中会根据配置信息初始化相应的TransactionFactory对象和DataSource对象

                TransactionFactory txFactory = transactionManagerElement(child.evalNode(&quot;transactionManager&quot;));

                DataSourceFactory dsFactory = dataSourceElement(child.evalNode(&quot;dataSource&quot;));

                DataSource dataSource = dsFactory.getDataSource();

                // 创建Environment对象，并关联创建好的TransactionFactory和DataSource

                Environment.Builder environmentBuilder = new Environment.Builder(id)

                        .transactionFactory(txFactory)

                        .dataSource(dataSource);

                // 将Environment对象记录到Configuration中，等待后续使用

                configuration.setEnvironment(environmentBuilder.build());

            }

        }

    }

}
</code></pre>
<h4>7. 处理<code>&lt;databaseIdProvider&gt;</code>标签</h4>
<p>通过前面课时的介绍可知，在 MyBatis 中编写的都是原生的 SQL 语句，而很多数据库产品都会有一些 SQL 方言，这些方言与标准 SQL 不兼容。</p>
<p>在 mybatis-config.xml 配置文件中，我们可以通过 <code>&lt;databaseIdProvider&gt;</code> 标签定义需要支持的全部数据库的 DatabaseId，在后续编写 Mapper 映射配置文件的时候，就可以为同一个业务场景定义不同的 SQL 语句（带有不同的 DataSourceId），来支持不同的数据库，这里就是靠 DatabaseId 来确定哪个 SQL 语句支持哪个数据库的。</p>
<p>databaseIdProviderElement() 方法是 XMLConfigBuilder 处理 <code>&lt;databaseIdProvider&gt;</code> 标签的地方，其中的<strong>核心就是获取 DatabaseId 值</strong>，具体实现如下：</p>
<pre><code>private void databaseIdProviderElement(XNode context) throws Exception {

    DatabaseIdProvider databaseIdProvider = null;

    if (context != null) {

        // 获取type属性值

        String type = context.getStringAttribute(&quot;type&quot;);

        if (&quot;VENDOR&quot;.equals(type)) { // 兼容操作

            type = &quot;DB_VENDOR&quot;;

        }

        // 初始化DatabaseIdProvider

        Properties properties = context.getChildrenAsProperties();

        databaseIdProvider = (DatabaseIdProvider) resolveClass(type).getDeclaredConstructor().newInstance();

        databaseIdProvider.setProperties(properties);

    }

    Environment environment = configuration.getEnvironment();

    if (environment != null &amp;&amp; databaseIdProvider != null) {

        // 通过DataSource获取DatabaseId，并保存到Configuration中，等待后续使用

        String databaseId = databaseIdProvider.getDatabaseId(environment.getDataSource());

        configuration.setDatabaseId(databaseId);

    }

}
</code></pre>
<p>可以看到，解析<code>&lt;databaseIdProvider&gt;</code> 标签之后会得到一个 DatabaseIdProvider 对象，其核心方法是 getDatabaseId() 方法，主要是根据前面解析得到的 DataSource 对象来生成 DatabaseId。DatabaseIdProvider 的继承关系如下图所示：</p>
<p><img src="assets/CioPOWA01E6AM0S_AAFq9Ci2CSc510.png" alt="2021223-1874.png" /></p>
<p>DatabaseIdProvider 继承关系图</p>
<p>从继承关系图中可以看出，DefaultDatabaseIdProvider 是个空实现，而且已被标记为过时了，所以这里我们就重点来看 VendorDatabaseIdProvider 实现。</p>
<p>在 getDatabaseId() 方法中，VendorDatabaseIdProvider 首先会从 DataSource 中拿到数据库的名称，然后根据 <code>&lt;databaseIdProvider&gt; </code>标签配置和 DataSource 返回的数据库名称，确定最终的 DatabaseId 标识，具体实现如下：</p>
<pre><code>public String getDatabaseId(DataSource dataSource) {

    // 省略边界检查和异常处理

    return getDatabaseName(dataSource);

}

private String getDatabaseName(DataSource dataSource) throws SQLException {

    // 从数据库连接中，获取数据库名称

    String productName = getDatabaseProductName(dataSource);

    if (this.properties != null) {

        // 根据&lt;databaseIdProvider&gt;标签配置，查找自定义数据库名称

        for (Map.Entry&lt;Object, Object&gt; property : properties.entrySet()) {

            if (productName.contains((String) property.getKey())) {

                return (String) property.getValue(); // 返回配置的value

            }

        }

        return null;

    }

    return productName;

}
</code></pre>
<h4>8. 处理<code>&lt;mappers&gt;</code>标签</h4>
<p>除了 mybatis-config.xml 这个全局配置文件之外，MyBatis 初始化的时候还会加载 <code>&lt;mappers&gt;</code> 标签下定义的 Mapper 映射文件。<code>&lt;mappers&gt;</code> 标签中会指定 Mapper.xml 映射文件的位置，通过解析 <code>&lt;mappers&gt; </code>标签，MyBatis 就能够知道去哪里加载这些 Mapper.xml 文件了。</p>
<p>mapperElement() 方法就是 XMLConfigBuilder 处理 <code>&lt;mappers&gt;</code> 标签的具体实现，其中会初始化 XMLMapperBuilder 对象来加载各个 Mapper.xml 映射文件。同时，还会扫描 Mapper 映射文件相应的 Mapper 接口，处理其中的注解并将 Mapper 接口注册到 MapperRegistry 中。</p>
<p>mapperElement() 方法的具体实现如下：</p>
<pre><code>private void mapperElement(XNode parent) throws Exception {

    if (parent != null) {

        for (XNode child : parent.getChildren()) { // 遍历每个子标签

            if (&quot;package&quot;.equals(child.getName())) {

                // 如果指定了&lt;package&gt;子标签，则会扫描指定包内全部Java类型

                String mapperPackage = child.getStringAttribute(&quot;name&quot;);

                configuration.addMappers(mapperPackage);

            } else {

                // 解析&lt;mapper&gt;子标签，这里会获取resource、url、class三个属性，这三个属性互斥

                String resource = child.getStringAttribute(&quot;resource&quot;);

                String url = child.getStringAttribute(&quot;url&quot;);

                String mapperClass = child.getStringAttribute(&quot;class&quot;);

                // 如果&lt;mapper&gt;子标签指定了resource或是url属性，都会创建XMLMapperBuilder对象，

                // 然后使用这个XMLMapperBuilder实例解析指定的Mapper.xml配置文件

                if (resource != null &amp;&amp; url == null &amp;&amp; mapperClass == null) {

                    ErrorContext.instance().resource(resource);

                    InputStream inputStream = Resources.getResourceAsStream(resource);

                    XMLMapperBuilder mapperParser = new XMLMapperBuilder(inputStream, configuration, resource, configuration.getSqlFragments());

                    mapperParser.parse();

                } else if (resource == null &amp;&amp; url != null &amp;&amp; mapperClass == null) {

                    ErrorContext.instance().resource(url);

                    InputStream inputStream = Resources.getUrlAsStream(url);

                    XMLMapperBuilder mapperParser = new XMLMapperBuilder(inputStream, configuration, url, configuration.getSqlFragments());

                    mapperParser.parse();

                } else if (resource == null &amp;&amp; url == null &amp;&amp; mapperClass != null) {

                    // 如果&lt;mapper&gt;子标签指定了class属性，则向MapperRegistry注册class属性指定的Mapper接口

                    Class&lt;?&gt; mapperInterface = Resources.classForName(mapperClass);

                    configuration.addMapper(mapperInterface);

                } else {

                    throw new BuilderException(&quot;A mapper element may only specify a url, resource or class, but not more than one.&quot;);

                }

            }

        }

    }

}
</code></pre>
<h3>总结</h3>
<p>这一讲我们重点介绍了 MyBatis 初始化过程中对 mybatis-config.xml 全局配置文件的解析，深入分析了 mybatis-config.xml 配置文件中所有标签的解析流程，让你进一步了解这些配置加载的原理。同时，我们还介绍了构造者模式这一经典设计模式，它是整个 MyBatis 初始化逻辑的基础思想。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;基于&#32;MyBatis&#32;缓存分析装饰器模式的最佳实践.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435719ea0f645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%20MyBatis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
