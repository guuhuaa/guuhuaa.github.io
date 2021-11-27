<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07  案例实战：使用 Spring Security 基础功能保护 Web 应用.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;Spring&#32;Security，为你的应用安全与职业之路保驾护航.md">00 开篇词  Spring Security，为你的应用安全与职业之路保驾护航.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;顶级框架：Spring&#32;Security&#32;是一款什么样的安全性框架？.md">01  顶级框架：Spring Security 是一款什么样的安全性框架？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;用户认证：如何使用&#32;Spring&#32;Security&#32;构建用户认证体系？.md">02  用户认证：如何使用 Spring Security 构建用户认证体系？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;认证体系：如何深入理解&#32;Spring&#32;Security&#32;用户认证机制？.md">03  认证体系：如何深入理解 Spring Security 用户认证机制？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;密码安全：Spring&#32;Security&#32;中包含哪些加解密技术？.md">04  密码安全：Spring Security 中包含哪些加解密技术？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;访问授权：如何对请求的安全访问过程进行有效配置？.md">05  访问授权：如何对请求的安全访问过程进行有效配置？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;权限管理：如何剖析&#32;Spring&#32;Security&#32;的授权原理？.md">06  权限管理：如何剖析 Spring Security 的授权原理？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="07&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;基础功能保护&#32;Web&#32;应用.md">07  案例实战：使用 Spring Security 基础功能保护 Web 应用.md</a>
                    

                </li>
                <li>

                    
                    <a href="08&#32;&#32;管道过滤：如何基于&#32;Spring&#32;Security&#32;过滤器扩展安全性？.md">08  管道过滤：如何基于 Spring Security 过滤器扩展安全性？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;攻击应对：如何实现&#32;CSRF&#32;保护和跨域&#32;CORS？.md">09  攻击应对：如何实现 CSRF 保护和跨域 CORS？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;全局方法：如何确保方法级别的安全访问？.md">10  全局方法：如何确保方法级别的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;高级主题保护&#32;Web&#32;应用.md">11  案例实战：使用 Spring Security 高级主题保护 Web 应用.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;开放协议：OAuth2&#32;协议解决的是什么问题？.md">12  开放协议：OAuth2 协议解决的是什么问题？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;授权体系：如何构建&#32;OAuth2&#32;授权服务器？.md">13  授权体系：如何构建 OAuth2 授权服务器？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;令牌扩展：如何使用&#32;JWT&#32;实现定制化&#32;Token？.md">15  令牌扩展：如何使用 JWT 实现定制化 Token？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;Spring&#32;Cloud&#32;构建微服务安全架构.md">16  案例实战：基于 Spring Security 和 Spring Cloud 构建微服务安全架构.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;OAuth2&#32;实现单点登录.md">17  案例实战：基于 Spring Security 和 OAuth2 实现单点登录.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;技术趋势：如何为&#32;Spring&#32;Security&#32;添加响应式编程特性？.md">18  技术趋势：如何为 Spring Security 添加响应式编程特性？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;测试驱动：如何基于&#32;Spring&#32;Security&#32;测试系统安全性？.md">19  测试驱动：如何基于 Spring Security 测试系统安全性？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;以终为始，Spring&#32;Security&#32;的学习总结.md">20 结束语  以终为始，Spring Security 的学习总结.md</a>

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
                        <div><h1>07  案例实战：使用 Spring Security 基础功能保护 Web 应用</h1>
<p>前面几讲我们系统地介绍了 Spring Security 的认证和授权功能，这是该框架为我们提供的最基础、也是最常用的安全性功能。作为阶段性的总结，今天我们就把前面几讲的内容整合在一起，基于 Spring Security 的认证和授权功能保护 Web 应用程序。</p>
<h3>案例设计和初始化</h3>
<p>在今天的案例中，我们将构建一个简单但完整的小型 Web 应用程序。当合法用户成功登录系统之后，浏览器会跳转到一个系统主页，并展示一些个人健康档案（HealthRecord）数据。</p>
<h4>案例设计</h4>
<p>这个 Web 应用程序将采用经典的三层架构，即<strong>Web 层、服务层和数据访问层</strong>，因此我们会存在 HealthRecordController、HealthRecordService 以及 HealthRecordRepository，这是一条独立的代码流程，用来完成<strong>系统业务逻辑处理</strong>。</p>
<p>另一方面，本案例的核心功能是<strong>实现自定义的用户认证流程</strong>，所以我们需要构建独立的 UserDetailsService 以及 AuthenticationProvider，这是另一条独立的代码流程。而在这条代码流程中，势必还需要 User 以及 UserRepository 等组件。</p>
<p>我们可以把这两条代码线整合在一起，得到案例的整体设计蓝图，如下图所示：</p>
<p><img src="assets/CioPOWDJyDOAKosUAACCwzt5aFc611.png" alt="Drawing 0.png" /></p>
<p>案例中的业务代码流程和用户认证流程</p>
<h4>系统初始化</h4>
<p>要想实现上图中的效果，我们需要先对系统进行初始化。这部分工作涉及<strong>领域对象的定义、数据库初始化脚本的整理以及相关依赖组件的引入</strong>。</p>
<p>针对领域对象，我们重点来看如下所示的 User 类定义：</p>
<pre><code>@Entity

public class User {

 

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Integer id;

 

    private String username;

    private String password;

 

    @Enumerated(EnumType.STRING)

    private PasswordEncoderType passwordEncoderType;

 

    @OneToMany(mappedBy = &quot;user&quot;, fetch = FetchType.EAGER)

	private List&lt;Authority&gt; authorities;

	…

}
</code></pre>
<p>可以看到，这里除了指定主键 id、用户名 username 和密码 password 之外，还包含了一个<strong>加密算法枚举值 EncryptionAlgorithm</strong>。在案例系统中，我们将提供 BCryptPasswordEncoder 和 SCryptPasswordEncoder 这两种可用的密码解密器，你可以通过该枚举值进行设置。</p>
<p>同时，我们在 User 类中还发现了一个 Authority 列表。显然，这个列表用来指定该 User 所具备的权限信息。Authority 类的定义如下所示：</p>
<pre><code>@Entity

public class Authority {

 

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Integer id;

 

    private String name;

 

    @JoinColumn(name = &quot;user&quot;)

    @ManyToOne

	private User user;

	…

}
</code></pre>
<p>通过定义不难看出 User 和 Authority 之间是<strong>一对多</strong>的关系，这点和 Spring Security 内置的用户权限模型是一致的。我们注意到这里使用了一系列来自 JPA（Java Persistence API，Java 持久化 API）规范的注解来定义领域对象之间的关联关系。关于这些注解的使用方式你可以参考拉勾教育上的[《Spring Data JPA 原理与实战》专栏]进行学习。</p>
<p>基于 User 和 Authority 领域对象，我们也给出创建数据库表的 SQL 定义，如下所示：</p>
<pre><code>CREATE TABLE IF NOT EXISTS `spring_security`.`user` (

  `id` INT NOT NULL AUTO_INCREMENT,

  `username` VARCHAR(45) NOT NULL,

  `password` TEXT NOT NULL,

  `password_encoder_type` VARCHAR(45) NOT NULL,

  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `spring_security`.`authority` (

  `id` INT NOT NULL AUTO_INCREMENT,

  `name` VARCHAR(45) NOT NULL,

  `user` INT NOT NULL,

  PRIMARY KEY (`id`));
</code></pre>
<p>在运行系统之前，我们同样也需要初始化数据，对应脚本如下所示：</p>
<pre><code>INSERT IGNORE INTO `spring_security`.`user` (`id`, `username`, `password`, `password_encoder_type`) VALUES ('1', 'jianxiang', '$2a$10$xn3LI/AjqicFYZFruSwve.681477XaVNaUQbr1gioaWPn4t1KsnmG', 'BCRYPT');

INSERT IGNORE INTO `spring_security`.`authority` (`id`, `name`, `user`) VALUES ('1', 'READ', '1');

INSERT IGNORE INTO `spring_security`.`authority` (`id`, `name`, `user`) VALUES ('2', 'WRITE', '1');

INSERT IGNORE INTO `spring_security`.`health_record` (`id`, `username`, `name`, `value`) VALUES ('1', 'jianxiang', 'weight', '70');

INSERT IGNORE INTO `spring_security`.`health_record` (`id`, `username`, `name`, `value`) VALUES ('2', 'jianxiang', 'height', '177');

INSERT IGNORE INTO `spring_security`.`health_record` (`id`, `username`, `name`, `value`) VALUES ('3', 'jianxiang', 'bloodpressure', '70');

INSERT IGNORE INTO `spring_security`.`health_record` (`id`, `username`, `name`, `value`) VALUES ('4', 'jianxiang', 'pulse', '80');
</code></pre>
<p>请注意，这里初始化了一个用户名为 “jianxiang”的用户，同时指定了它的密码为“12345”，加密算法为“BCRYPT”。</p>
<p>现在，领域对象和数据层面的初始化工作已经完成了，接下来我们需要在代码工程的 pom 文件中添加如下所示的 Maven 依赖：</p>
<pre><code>&lt;dependencies&gt;	    

        &lt;dependency&gt;

            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

            &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;

        &lt;/dependency&gt;

        &lt;dependency&gt;

            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

            &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;

        &lt;/dependency&gt;

        &lt;dependency&gt;

            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

            &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;

        &lt;/dependency&gt;

        &lt;dependency&gt;

            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;

        &lt;/dependency&gt;

 

        &lt;dependency&gt;

            &lt;groupId&gt;mysql&lt;/groupId&gt;

            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;

            &lt;scope&gt;runtime&lt;/scope&gt;

        &lt;/dependency&gt;

        &lt;dependency&gt;

            &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;

            &lt;artifactId&gt;spring-security-test&lt;/artifactId&gt;

            &lt;scope&gt;test&lt;/scope&gt;

        &lt;/dependency&gt;

&lt;/dependencies&gt;
</code></pre>
<p>这些依赖包都是很常见的，相信从包名中你就能明白各依赖包的作用。</p>
<blockquote>
<p>依赖包参考链接：
spring-boot-starter-data-jpa：<a href="https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-data-jpa?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-data-jpa</a>
spring-boot-starter-security：<a href="https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-security?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-security</a>
spring-boot-starter-thymeleaf：<a href="https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf</a>
spring-boot-starter-web：<a href="https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web</a>
mysql-connector-java：<a href="https://mvnrepository.com/artifact/mysql/mysql-connector-java?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/mysql/mysql-connector-java</a>
spring-security-test：<a href="https://mvnrepository.com/artifact/org.springframework.security/spring-security-test?fileGuid=xxQTRXtVcqtHK6j8">https://mvnrepository.com/artifact/org.springframework.security/spring-security-test</a></p>
</blockquote>
<h3>实现自定义用户认证</h3>
<p>实现自定义用户认证的过程通常涉及两大部分内容，一方面需要使用 User 和 Authority 对象来完成<strong>定制化的用户管理</strong>，另一方面需要把这个定制化的用户管理<strong>嵌入整个用户认证流程中</strong>。下面我们分别详细分析。</p>
<h4>实现用户管理</h4>
<p>我们知道在 Spring Security 中，代表用户信息的就是 UserDetails 接口。我们也在[ 03讲 “认证体系：如何深入理解 Spring Security 的用户认证机制？”]中介绍过 UserDetails 接口的具体定义。如果你想实现自定义的用户信息，扩展这个接口即可。实现方式如下所示：</p>
<pre><code>public class CustomUserDetails implements UserDetails {

 

    private final User user;

 

    public CustomUserDetails(User user) {

        this.user = user;

    }

 

    @Override

    public Collection&lt;? extends GrantedAuthority&gt; getAuthorities() {

        return user.getAuthorities().stream()

                   .map(a -&gt; new SimpleGrantedAuthority(a.getName()))

                   .collect(Collectors.toList());

    }

 

    @Override

    public String getPassword() {

        return user.getPassword();

    }

 

    @Override

    public String getUsername() {

        return user.getUsername();

    }

 

    @Override

    public boolean isAccountNonExpired() {

        return true;

    }

 

    @Override

    public boolean isAccountNonLocked() {

        return true;

    }

 

    @Override

    public boolean isCredentialsNonExpired() {

        return true;

    }

 

    @Override

    public boolean isEnabled() {

        return true;

    }

 

    public final User getUser() {

        return user;

    }

}
</code></pre>
<p>上述 CustomUserDetails 类实现了 UserDetails 接口中约定的所有需要实现的方法。请注意，这里的 getAuthorities() 方法中，我们将 User 对象中的 Authority 列表转换为了 Spring Security 中代表用户权限的<strong>SimpleGrantedAuthority 列表</strong>。</p>
<p>当然，所有的自定义用户信息和权限信息都是维护在数据库中的，所以为了获取这些信息，我们需要创建数据访问层组件，这个组件就是 UserRepository，定义如下：</p>
<pre><code>public interface UserRepository extends JpaRepository&lt;User, Integer&gt; {

 

    Optional&lt;User&gt; findUserByUsername(String username);

}
</code></pre>
<p>这里只是简单扩展了 Spring Data JPA 中的 JpaRepository 接口，并使用<strong>方法名衍生查询机制</strong>定义了根据用户名获取用户信息的 findUserByUsername 方法。</p>
<p>现在，我们已经能够在数据库中维护自定义用户信息，也能够根据这些用户信息获取到 UserDetails 对象，那么接下来要做的事情就是扩展 UserDetailsService。自定义 CustomUserDetailsService 实现如下所示：</p>
<pre><code>@Service

public class CustomUserDetailsService implements UserDetailsService {

 

    @Autowired

    private UserRepository userRepository;

 

    @Override

    public CustomUserDetails loadUserByUsername(String username) {

        Supplier&lt;UsernameNotFoundException&gt; s =

                () -&gt; new UsernameNotFoundException(&quot;Username&quot; + username + &quot;is invalid!&quot;);

 

        User u = userRepository.findUserByUsername(username).orElseThrow(s);

 

        return new CustomUserDetails(u);

    }

}
</code></pre>
<p>这里我们通过 UserRepository 查询数据库来获取 CustomUserDetails 信息，如果传入的用户名没有对应的 CustomUserDetails 则会抛出异常。</p>
<h4>实现认证流程</h4>
<p>我们再次回顾 AuthenticationProvider 的接口定义，如下所示：</p>
<pre><code>public interface AuthenticationProvider {

 

    //执行认证，返回认证结果

    Authentication authenticate(Authentication authentication)

             throws AuthenticationException;

 

    //判断是否支持当前的认证对象

    boolean supports(Class&lt;?&gt; authentication);

}
</code></pre>
<p>实现自定义认证流程要做的也是实现 AuthenticationProvider 中的这两个方法，而认证过程势必要借助于前面介绍的 CustomUserDetailsService。</p>
<p>我们先来看一下 AuthenticationProvider 接口的实现类 AuthenticationProviderService，如下所示：</p>
<pre><code>@Service

public class AuthenticationProviderService implements AuthenticationProvider {

 

    @Autowired

    private CustomUserDetailsService userDetailsService;

 

    @Autowired

    private BCryptPasswordEncoder bCryptPasswordEncoder;

 

    @Autowired

    private SCryptPasswordEncoder sCryptPasswordEncoder;

 

    @Override

    public Authentication authenticate(Authentication authentication) throws AuthenticationException {

        String username = authentication.getName();

        String password = authentication.getCredentials().toString();

 

        //根据用户名从数据库中获取 CustomUserDetails

        CustomUserDetails user = userDetailsService.loadUserByUsername(username);

 

        //根据所配置的密码加密算法分别验证用户密码

        switch (user.getUser().getPasswordEncoderType()) {

            case BCRYPT:

                return checkPassword(user, password, bCryptPasswordEncoder);

            case SCRYPT:

                return checkPassword(user, password, sCryptPasswordEncoder);

        }

 

        throw new  BadCredentialsException(&quot;Bad credentials&quot;);

    }

 

    @Override

    public boolean supports(Class&lt;?&gt; aClass) {

        return UsernamePasswordAuthenticationToken.class.isAssignableFrom(aClass);

    }

 

    private Authentication checkPassword(CustomUserDetails user, String rawPassword, PasswordEncoder encoder) {

        if (encoder.matches(rawPassword, user.getPassword())) {

            return new UsernamePasswordAuthenticationToken(user.getUsername(), user.getPassword(), user.getAuthorities());

        } else {

            throw new BadCredentialsException(&quot;Bad credentials&quot;);

        }

    }

}
</code></pre>
<p>AuthenticationProviderService 类虽然看起来比较长，但代码基本都是自解释的。我们首先通过 CustomUserDetailsService 从数据库中获取用户信息并构造成 CustomUserDetails 对象。然后，根据指定的密码加密器对用户密码进行验证，如果验证通过则构建一个 UsernamePasswordAuthenticationToken 对象并返回，反之直接抛出 BadCredentialsException 异常。而在 supports() 方法中指定的就是这个目标 UsernamePasswordAuthenticationToken 对象。</p>
<h4>安全配置</h4>
<p>最后，我们要做的就是通过 Spring Security 提供的配置体系将前面介绍的所有内容串联起来，如下所示：</p>
<pre><code>@Configuration

public class SecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Autowired

    private AuthenticationProviderService authenticationProvider;

 

    @Bean

    public BCryptPasswordEncoder bCryptPasswordEncoder() {

        return new BCryptPasswordEncoder();

    }

 

    @Bean

    public SCryptPasswordEncoder sCryptPasswordEncoder() {

        return new SCryptPasswordEncoder();

    }

 

    @Override

    protected void configure(AuthenticationManagerBuilder auth) {

        auth.authenticationProvider(authenticationProvider);

    }

 

    @Override

    protected void configure(HttpSecurity http) throws Exception {

        http.formLogin()

            .defaultSuccessUrl(&quot;/healthrecord&quot;, true);

        http.authorizeRequests().anyRequest().authenticated();

    }

}
</code></pre>
<p>这里注入了已经构建完成的 AuthenticationProviderService，并初始化了两个密码加密器 BCryptPasswordEncoder 和 SCryptPasswordEncoder。最后，我们覆写了 WebSecurityConfigurerAdapter 配置适配器类中的 configure() 方法，并指定用户登录成功后将跳转到&quot;/main&quot;路径所指定的页面。</p>
<p>对应的，我们需要构建如下所示的 MainController 类来指定&quot;/main&quot;路径，并展示业务数据的获取过程，如下所示：</p>
<pre><code>@Controller

public class HealthRecordController {

    @Autowired

    private HealthRecordService healthRecordService;

    

    @GetMapping(&quot;/healthrecord&quot;)

    public String main(Authentication a, Model model) {

        String userName = a.getName();

        model.addAttribute(&quot;username&quot;, userName);

        model.addAttribute(&quot;healthRecords&quot;, healthRecordService.getHealthRecordsByUsername(userName));

        return &quot;health_record.html&quot;;

    }

}
</code></pre>
<p>我们通过 Authentication 对象获取了认证用户信息，同时通过 HealthRecordService 获取了健康档案信息。关于 HealthRecordService 的实现逻辑不是今天内容的重点，你可以参考案例源码进行学习：<a href="https://github.com/lagouEdAnna/SpringSecurity-jianxiang/tree/main/SpringSecurityBasicDemo?fileGuid=xxQTRXtVcqtHK6j8">https://github.com/lagouEdAnna/SpringSecurity-jianxiang/tree/main/SpringSecurityBasicDemo</a>。</p>
<p>请注意，这里所指定的 health_record.html 位于 resources/templates 目录下，该页面基于 thymeleaf 模板引擎构建，如下所示：</p>
<pre><code>&lt;!DOCTYPE html&gt;

&lt;html lang=&quot;en&quot; xmlns:th=&quot;http://www.thymeleaf.org&quot;&gt;

    &lt;head&gt;

        &lt;meta charset=&quot;UTF-8&quot;&gt;

        &lt;title&gt;健康档案&lt;/title&gt;

    &lt;/head&gt;

    &lt;body&gt;

        &lt;h2 th:text=&quot;'登录用户：' + ${username}&quot; /&gt;

        &lt;p&gt;&lt;a href=&quot;/logout&quot;&gt;退出登录&lt;/a&gt;&lt;/p&gt;

        &lt;h2&gt;个人健康档案:&lt;/h2&gt;

        &lt;table&gt;

            &lt;thead&gt;

            &lt;tr&gt;

                &lt;th&gt; 健康指标名称 &lt;/th&gt;

                &lt;th&gt; 健康指标值 &lt;/th&gt;

            &lt;/tr&gt;

            &lt;/thead&gt;

            &lt;tbody&gt;

            &lt;tr th:if=&quot;${healthRecords.empty}&quot;&gt;

                &lt;td colspan=&quot;2&quot;&gt; 无健康指标 &lt;/td&gt;

            &lt;/tr&gt;

            &lt;tr th:each=&quot;healthRecord : ${healthRecords}&quot;&gt;

                &lt;td&gt;&lt;span th:text=&quot;${healthRecord.name}&quot;&gt; 健康指标名称 &lt;/span&gt;&lt;/td&gt;

                &lt;td&gt;&lt;span th:text=&quot;${healthRecord.value}&quot;&gt; 健康指标值 &lt;/span&gt;&lt;/td&gt;

            &lt;/tr&gt;

            &lt;/tbody&gt;

        &lt;/table&gt;

    &lt;/body&gt;

&lt;/html&gt;
</code></pre>
<p>这里我们从 Model 对象中获取了认证用户信息以及健康档案信息，并渲染在页面上。</p>
<h3>案例演示</h3>
<p>现在，让我们启动 Spring Boot 应用程序，并访问<a href="http://localhost:8080/?fileGuid=xxQTRXtVcqtHK6j8">http://localhost:8080</a>端点。因为访问系统的任何端点都需要认证，所以 Spring Security 会自动跳转到如下所示的登录界面：</p>
<p><img src="assets/CioPOWDJyFCAWC1SAAA5aEhV0-A820.png" alt="Drawing 1.png" /></p>
<p>用户登录界面</p>
<p>我们分别输入用户名“jianxiang”和密码“12345”，系统就会跳转到健康档案主页：</p>
<p><img src="assets/CioPOWDJyFeAUaWEAAB7TB8wdKw208.png" alt="Drawing 2.png" /></p>
<p>健康档案主页</p>
<p>在这个主页中，我们正确获取了登录用户的用户名，并展示了个人健康档案信息。这个结果也证实了自定义用户认证体系的正确性。你可以根据示例代码做一些尝试。</p>
<h3>小结与预告</h3>
<p>这一讲我们动手实践了“利用 Spring Security 基础功能保护 Web 应用程序”。综合第 2 讲到 6 讲中的核心知识点，我们设计了一个简单而又完整的案例，并通过构建用户管理和认证流程讲解了实现自定义用户认证机制的过程。</p>
<p>本讲内容总结如下：</p>
<p><img src="assets/Cgp9HWDJyF6AAUtVAACuoKgyiho485.png" alt="Drawing 3.png" /></p>
<p>最后给你留一道思考题：在 Spring Security 中，实现一套自定义的用户认证体系需要哪些开发步骤？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;&#32;权限管理：如何剖析&#32;Spring&#32;Security&#32;的授权原理？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;&#32;管道过滤：如何基于&#32;Spring&#32;Security&#32;过滤器扩展安全性？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434da0fdef70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Security%20%E8%AF%A6%E8%A7%A3%E4%B8%8E%E5%AE%9E%E6%93%8D/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
