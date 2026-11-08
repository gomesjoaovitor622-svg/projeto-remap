import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:http/http.dart' as http;

const apiBaseUrl = String.fromEnvironment('API_BASE_URL', defaultValue: 'http://10.0.2.2:8000');
const secureStorage = FlutterSecureStorage();
void main() => runApp(const RemapApp());

class RemapApp extends StatelessWidget {
  const RemapApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(title: 'REMAP', debugShowCheckedModeBanner: false, theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF6C4CF1)), useMaterial3: true, scaffoldBackgroundColor: const Color(0xFFF6F7FB)), home: const LoginPage());
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();
  final _email = TextEditingController();
  final _password = TextEditingController();
  final _organization = TextEditingController();
  bool _loading = false;
  bool _obscure = true;
  String? _error;
  @override
  void dispose() { _email.dispose(); _password.dispose(); _organization.dispose(); super.dispose(); }

  Future<void> _login() async {
    if (!_formKey.currentState!.validate()) return;
    setState(() { _loading = true; _error = null; });
    try {
      final response = await http.post(Uri.parse('$apiBaseUrl/api/v1/auth/login'), headers: {'Content-Type': 'application/json'}, body: jsonEncode({'email': _email.text.trim(), 'password': _password.text, if (_organization.text.trim().isNotEmpty) 'organization_slug': _organization.text.trim()})).timeout(const Duration(seconds: 15));
      if (response.statusCode != 200) throw Exception('Não foi possível entrar. Confira os dados e a empresa.');
      final token = jsonDecode(response.body)['access_token'] as String;
      await secureStorage.write(key: 'remap_access_token', value: token);
      if (!mounted) return;
      Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const HomePage()));
    } catch (e) {
      if (mounted) setState(() => _error = e.toString().replaceFirst('Exception: ', ''));
    } finally { if (mounted) setState(() => _loading = false); }
  }

  @override
  Widget build(BuildContext context) => Scaffold(body: SafeArea(child: Center(child: SingleChildScrollView(padding: const EdgeInsets.all(24), child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 440), child: Card(elevation: 0, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(28)), child: Padding(padding: const EdgeInsets.all(28), child: Form(key: _formKey, child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
    Container(width: 64, height: 64, decoration: BoxDecoration(color: Theme.of(context).colorScheme.primaryContainer, borderRadius: BorderRadius.circular(20)), child: Icon(Icons.car_repair_rounded, size: 34, color: Theme.of(context).colorScheme.primary)),
    const SizedBox(height: 24), Text('REMAP', style: Theme.of(context).textTheme.headlineMedium?.copyWith(fontWeight: FontWeight.w800, letterSpacing: 2)),
    const SizedBox(height: 6), Text('Gestão e diagnóstico automotivo', style: Theme.of(context).textTheme.bodyMedium?.copyWith(color: Colors.black54)),
    const SizedBox(height: 28), TextFormField(controller: _email, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(labelText: 'E-mail', prefixIcon: Icon(Icons.email_outlined), border: OutlineInputBorder()), validator: (v) => v == null || !v.contains('@') ? 'Informe um e-mail válido.' : null),
    const SizedBox(height: 14), TextFormField(controller: _organization, decoration: const InputDecoration(labelText: 'Empresa (identificador)', prefixIcon: Icon(Icons.business_outlined), border: OutlineInputBorder(), helperText: 'Deixe vazio somente para acesso global.')),
    const SizedBox(height: 14), TextFormField(controller: _password, obscureText: _obscure, decoration: InputDecoration(labelText: 'Senha', prefixIcon: const Icon(Icons.lock_outline), suffixIcon: IconButton(onPressed: () => setState(() => _obscure = !_obscure), icon: Icon(_obscure ? Icons.visibility_outlined : Icons.visibility_off_outlined)), border: const OutlineInputBorder()), validator: (v) => v == null || v.isEmpty ? 'Informe sua senha.' : null),
    if (_error != null) ...[const SizedBox(height: 14), Text(_error!, style: const TextStyle(color: Colors.red), textAlign: TextAlign.center)],
    const SizedBox(height: 22), FilledButton.icon(onPressed: _loading ? null : _login, icon: _loading ? const SizedBox(width: 18, height: 18, child: CircularProgressIndicator(strokeWidth: 2)) : const Icon(Icons.login), label: Text(_loading ? 'Entrando...' : 'Entrar'), style: FilledButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))),
    const SizedBox(height: 20), const Text('Acesso protegido • REMAP', textAlign: TextAlign.center, style: TextStyle(color: Colors.black45, fontSize: 12)),
  ]))))))));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});
  @override
  Widget build(BuildContext context) => Scaffold(appBar: AppBar(title: const Text('REMAP')), body: Center(child: Padding(padding: const EdgeInsets.all(24), child: Column(mainAxisSize: MainAxisSize.min, children: [const Icon(Icons.check_circle_outline, size: 56), const SizedBox(height: 16), Text('Acesso autenticado', style: Theme.of(context).textTheme.headlineSmall), const SizedBox(height: 8), const Text('A estrutura inicial está pronta. Os módulos de veículos, ECUs e diagnósticos serão adicionados nas próximas etapas.'), const SizedBox(height: 20), OutlinedButton.icon(onPressed: () async { await secureStorage.delete(key: 'remap_access_token'); if (context.mounted) Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const LoginPage())); }, icon: const Icon(Icons.logout), label: const Text('Sair'))]))));
}
