import 'package:flutter_test/flutter_test.dart';
import 'package:remap_mobile/main.dart';
void main() {
  testWidgets('exibe a tela inicial de login do REMAP', (tester) async {
    await tester.pumpWidget(const RemapApp());
    expect(find.text('REMAP'), findsOneWidget);
    expect(find.text('Gestão e diagnóstico automotivo'), findsOneWidget);
    expect(find.text('Entrar'), findsOneWidget);
  });
}
