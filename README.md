#Editing test by RokyZevon


#EasyCMS

## 描述

一个极简的内容发布管理系统（CMS），使用Python的Flask框架，力求做一个通用性但不失轻量的CMS。

## 功能模块

### 用户

 + 添加用户
 + 用户管理

#### 权限分级

 + 管理员
 + 编辑
 + 作者
 + 订阅者

#### 权限划分

 + 修改网站信息（管理员）
 + 发布文章和页面（编辑及其以上）
 + 发布/编辑文章和页面（作者及其以上，作者修改会进草稿箱）
 + 添加分类（作者及其以上）
 + 分类管理（编辑及其以上）
 + 添加标签（作者及其以上）
 + 标签管理（编辑及其以上）
 + 查看隐私文章（订阅及其以上）

### 文章

 + 文章发布
 + 文章修改
 + 文章管理

### 页面
 
 + 页面发布
 + 页面修改
 + 页面管理

### 文章分类
 
 + 添加分类
 + 分类管理

### 标签

 + 添加标签
 + 标签管理

## 数据库设计

![db](https://raw.githubusercontent.com/Coderhypo/EasyCMS/master/db.png)

使用了SQLAlchemy模块，model类设计如下：

### 用户表

```
class User(db.Model):

    '''用户表'''

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(64), unique=True, nullable=False)
    user_nicename = db.Column(db.String(64), unique=True)
    user_pass = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), unique=True, nullable=False)
    user_url = db.Column(db.String(64))
    user_rule = db.Column(db.Integer)

    posts = db.relationship('Post', backref='user')
    pages = db.relationship('Page', backref='user')

    def __repr__(self):
        return '<Users %r>' % self.user_id

```

### 文章表

```
class Post(db.Model):

    '''文章表'''

    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.Text, nullable=False)
    post_content = db.Column(db.Text)
    post_status = db.Column(db.Integer, nullable=False)
    post_password = db.Column(db.String(64))
    post_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    postmetas = db.relationship('Postmeta', backref='post')
    postlabels = db.relationship('Postlabel', backref='post')

    def __repr__(self):
        return '<Post % r>' % self.post_id
```

### 页面表

```
class Page(db.Model):

    '''页面表'''

    __tablename__ = 'pages'
    page_id = db.Column(db.Integer, primary_key=True)
    page_title = db.Column(db.Text, nullable=False)
    page_content = db.Column(db.Text)
    page_status = db.Column(db.Integer)
    page_password = db.Column(db.String(64))
    page_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return '<Page % r>' % self.page_id
```

### 文章分类

#### 分类表

```
class Meta(db.Model):

    '''文章分类表'''

    __tablename__ = 'metas'
    meta_id = db.Column(db.Integer, primary_key=True)
    meta_name = db.Column(db.String(64), nullable=False, unique=True)
    meta_slug = db.Column(db.String(64), nullable=False, unique=True)
    meta_describe = db.Column(db.Text)

    postmetas = db.relationship('Postmeta',backref='meta')

    def __repr__(self):
        return '<Meta %r>' % self.meta_id
```

#### 分类明细表

```
class Postmeta(db.Model):

    '''文章分类明细表'''

    __tablename__ = 'postmetas'
    id = db.Column(db.Integer, primary_key=True)
    meta_id = db.Column(db.Integer, db.ForeignKey('metas.meta_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))

    def __repr__(self):
        return '<PostMeta postId:%r = metaId:%r>' % (self.post_id,self.meta_id)
```

### 文章标签

#### 标签表

```
class Label(db.Model):

    '''标签表'''

    __tablename__ = 'labels'
    label_id = db.Column(db.Integer, primary_key=True)
    label_name = db.Column(db.String(60), nullable=False, unique=True)
    label_slug = db.Column(db.String(60), nullable=False, unique=True)

    postlabels = db.relationship('Postlabel', backref='label')

    def __repr__(self):
        return '<Label %r>' % self.label_id
```

#### 文章标签表

```
class Postlabel(db.Model):

    '''文章，标签对应表'''

    __tablename__ = 'psotlabels'
    id = db.Column(db.Integer, primary_key=True)
    label_id = db.Column(db.Integer, db.ForeignKey('labels.label_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))

    def __repr__(self):
        return '<Postlabel postId:%r == labelId:%r>' % (self.post_id,self.label_id)

```


